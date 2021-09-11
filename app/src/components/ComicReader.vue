<template>
	<div class="comic" :style="bottomMargin">
		<custom-loading :show="isLoadingImagesBefore"/>
		<comic-page
			:src="page.url"
			:display-mode="displayMode"
			:zoom-scale="zoomScale"
			v-for="page in pages"
			:index="page.index"
			:key="page.index"
			@load="handleImageLoaded"
			:show="page.isVisible"
		/>
		<custom-loading :show="isLoadingImagesAfter"/>
	</div>
</template>

<script>
import ComicPage from './../components/ComicPage.vue'
import CustomLoading from './../components/CustomLoading.vue'
import MouseScrollDrag from './../utils/MouseScrollDrag.js'
import MouseEvents from './../utils/MouseEvents.js'

const PAGE_MARGIN_TOP = 8;
const BOTTOM_BAR_HEIGHT_PLUS_MARGIN = 48;

export default {
	name: 'ComicReader',
	props: {
		pages: [],
		page: {
			type: Number,
			default: 0
		},
		numPages: {
			type: Number,
			default: 0
		},
		remainImagesToTrigger: {
			type: Number,
			default: 0
		},
		displayMode: {
			type: String
		},
		zoomScale: { type: Number, default: 1
		},
		bottomSpacing: {
			type: Boolean,
			default: true
		},
		isLoadingComic: {
			type: Boolean,
			default: true
		},
		isLoadingImagesBefore: {
			type: Boolean,
			default: false
		},
		isLoadingImagesAfter: {
			type: Boolean,
			default: false
		}
	},
	data() {
		return {
			mouseScrollDrag: null,
			mouseEvents: null,
			isSetupDone: false,
			isInfiniteScrollEnabled: false
		}
	},
	computed: {
		bottomMargin() {
			const paddingBottom = this.bottomSpacing ? BOTTOM_BAR_HEIGHT_PLUS_MARGIN : 0;
			return {
				paddingBottom
			}
		}
	},
	methods: {
		handleImageLoaded(pageImage) {
			this.$emit('page-load', pageImage);
		},
		calculatePageHeight(pageHeight) {
			switch(this.displayMode) {
				case "fit-height":
					return window.innerHeight;
				case "fit-width":
					return window.innerWidth;
				case "zoom":
					return this.zoomScale * pageHeight;
			}

			return pageHeight;
		},
		getCurrentPageByScrollPosition() {
			const visiblePages = this.pages.filter(page => page.isVisible);
			const scrollY = Math.max(0, window.scrollY);
			let comicHeight = 0;

			for(let i = 0; i < visiblePages.length; i++) {
				const page = visiblePages[i];
				const pageHeight = this.calculatePageHeight(page.height);
				const comicHalfPage = comicHeight + (pageHeight + PAGE_MARGIN_TOP) / 2;

				if(scrollY <= comicHalfPage) {
					return page.index;
				}

				comicHeight += pageHeight + PAGE_MARGIN_TOP;
			}

			if(visiblePages.length === 0) {
				return 0;
			}

			return visiblePages[visiblePages.length - 1].index;
		},
		handleScrollPositionChange() {
			if(!this.isInfiniteScrollEnabled) return;

			const currentPage = this.getCurrentPageByScrollPosition();

			if(currentPage != this.page) {
				this.onPageChange(currentPage);
			}
		},
		onPageChange(newPage) {
			this.$emit("page-change", newPage);

			this.processPageChange(newPage);
		},
		processPageChange(newPage) {
			const visiblePages = this.pages.filter(page => page.isVisible);
			const numVisiblePages = visiblePages.length;

			if(numVisiblePages > 0 && numVisiblePages < this.numPages) {
				const firstPageIndex = visiblePages[0].index;
				const lastPageIndex = visiblePages[visiblePages.length - 1].index;
				const loadAfterThreshold = newPage + this.remainImagesToTrigger;
				const loadBeforeThreshold = newPage - this.remainImagesToTrigger;
				
				if(loadAfterThreshold >= lastPageIndex && lastPageIndex < this.numPages) {
					this.$emit("load-more", true);
				}

				if(loadBeforeThreshold <= firstPageIndex && firstPageIndex  > 1) {
					this.$emit("load-more", false);
				}
			}
		},
		handleComicLoaded() {
			const currentPage = this.pages.find(page => page.index === this.page);

			if(currentPage) {
				const rootElementTop = this.$el.getBoundingClientRect().top + window.scrollY;
				const imgTop = currentPage.img.getBoundingClientRect().top;
				const elementScrollPos = imgTop + window.scrollY - rootElementTop - PAGE_MARGIN_TOP;

				this.scrollTargetPosition = elementScrollPos;

				setTimeout(() => {
					window.scroll({
						top: elementScrollPos,
						behavior: 'auto'
					})

					this.onScrollStoppedMoving();
				}, 250);
			} else {
				this.onScrollStoppedMoving();
			}
		},
		onScrollStoppedMoving() {
			this.onReady();
		},
		onReady() {
			this.isInfiniteScrollEnabled = true;
			this.mouseScrollDrag.setEnabled(true);
			this.$emit("ready");
		}
	},
	watch: {
		isLoadingComic(val) {
			if(!val) {
				this.handleComicLoaded();
			}
		}
	},
	mounted() {
		const rootElement = this.$el;

		this.mouseEvents = new MouseEvents(rootElement);

		this.mouseEvents.onClick = () => {
			this.$emit('click');
		}

		this.mouseEvents.onDoubleClick = () => {
			this.$emit('dblclick');
		}

		this.mouseScrollDrag = new MouseScrollDrag(rootElement);

		document.addEventListener('scroll', () => {
			this.handleScrollPositionChange();
		});
	},
	components: {
		ComicPage,
		CustomLoading
	}
};
</script>

<style scoped>
.comic {
	position: relative;
	min-height: 100vh;
	background-color: #212121;
	padding-top: 8px;
	padding-left: 8px;
}

.comic {
	width: 100%;
	position: absolute;
	top: 0;
	overflow: auto;
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	text-align: center;
}

.comic:active {
	cursor: grabbing;
}

.comic .page + .page {
	margin-top: 8px;
}

</style>
