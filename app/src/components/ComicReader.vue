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
		remainImagesTrigger: {
			type: Number,
			default: 0
		},
		displayMode: {
			type: String
		},
		zoomScale: {
			type: Number,
			default: 1
		},
		bottomSpacing: {
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
			mouseEvents: null
		}
	},
	computed: {
		bottomMargin() {
			return {
				paddingBottom: (8 + (this.bottomSpacing ? 48 : 0)) + 'px' 
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
		getCurrentPage(scrollY) {
			let comicHeight = 0;

			for(let i = 0; i < this.pages.length; i++) {
				const page = this.pages[i];
				const pageHeight = this.calculatePageHeight(page.height);

				if(scrollY <= comicHeight + (pageHeight + 8) / 2) {
					return page.index;
				}

				comicHeight += pageHeight + 8;
			}

			return this.numPages;
		},
		handleScrollPositionChange() {
			const scrollPosition = window.scrollY;
			let scrollY = scrollPosition;

			if(scrollY <= 0) {
				scrollY = 0;
			}

			const currentPage = this.getCurrentPage(scrollY);

			if(currentPage != this.page) {
				this.onPageChange(currentPage);
			}
		},
		onPageChange(newPage) {
			this.$emit("page-change", newPage);

			const visiblePages = this.pages.filter(page => page.isVisible);

			if(visiblePages.length && visiblePages.length < this.numPages) {
				if(newPage + this.remainImagesTrigger >= visiblePages[visiblePages.length - 1].index &&
					visiblePages[visiblePages.length - 1].index < this.numPages) {
					this.$emit("load-more", true);
				}

				if(newPage - this.remainImagesTrigger <= visiblePages[0].index && 
					visiblePages[0].index > 1) {
					this.$emit("load-more", false);
				}
			}
		}
	},
	mounted() {
		const rootElement = this.$el;

		this.mouseScrollDrag = new MouseScrollDrag(rootElement);
		this.mouseEvents = new MouseEvents(rootElement);

		this.mouseEvents.onClick = () => {
			this.$emit('click');
		}

		this.mouseEvents.onDoubleClick = () => {
			this.$emit('dblclick');
		}

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
