<template>
	<v-app>
		<v-app-bar app dark color="primary" v-if="isControlsEnabled">
			<v-toolbar-title class="title">Vol 1 - Romance Dawn</v-toolbar-title>
			<v-spacer/>
			<v-menu offset-y>
				<template v-slot:activator="{ on, attrs }">
					<v-btn 
						icon
						v-bind="attrs"
						v-on="on"
					>
						<v-icon>mdi-cog</v-icon>
					</v-btn>
				</template>
				<v-list>
					<v-list-item link @click="setDisplayMode('fit-height')">
						Adjust to height
					</v-list-item>
					<v-list-item link @click="setDisplayMode('fit-width')">
						Adjust to width
					</v-list-item>
					<v-list-item>
						<div class="config__item">
							<span>Zoom</span>
							<zoom-control :zoom-scale="zoomScale" @change="handleZoomControlChange"/>
						</div>
					</v-list-item>
				</v-list>
			</v-menu>
		</v-app-bar>
		<v-main>
			<div :class="mainWrapperClassObject">
				<comic-reader
					@click="handleComicReaderClick"
					@dblclick="handleComicReaderDoubleClick"
					:display-mode="displayMode"
					:zoom-scale="normalizedZoomScale"
					:bottom-spacing="isControlsEnabled"
					:page="page"
					:num-pages="numPages"
					:remain-images-to-trigger="remainImagesToTrigger"
					:pages="pages"
					:is-loading-images-before="isLoadingImagesBefore"
					:is-loading-images-after="isLoadingImagesAfter"
					:is-loading-comic="isLoadingComic"
					@page-load="handlePageLoaded"
					@page-change="handleComicReaderPageChange"
					@load-more="handleComicReaderLoadMore"
					@ready="handleComicReaderReady"
				/>
			</div>
			<loading :show="isLoadingComic && !isComicReaderReady" />
		</v-main>
		<v-app-bar
			fixed
			color="primary"
			dark
			bottom
			dense
			width="100%"
			v-if="isControlsEnabled"
		>
			<div class="options">
				<page-counter :page="page" :max-pages="numPages" />
			</div>
		</v-app-bar>
	</v-app>
</template>

<script>
import PageCounter from './../components/PageCounter.vue'
import ZoomControl from './../components/ZoomControl.vue'
import ComicReader from './../components/ComicReader.vue'
import Loading from './../components/Loading.vue'

export default {
	name: 'ReadComic',
	components: {
		PageCounter,
		ZoomControl,
		ComicReader,
		Loading
	},
	data() {
		return {
			isControlsEnabled: true,
			displayMode: '',
			zoomScale: 100,
			page: 10,
			numPages: 20,
			remainImagesToTrigger: 3,
			numPreloadedImages: 5,
			pages: [],
			pagesLoadingBefore: [],
			pagesLoadingAfter: [],
			pagesLoadedBefore: [],
			pagesLoadedAfter: [],
			isLoadingImagesBefore: false,
			isLoadingImagesAfter: false,
			isLoadingComic: true,
			isComicReaderReady: false
		};
	},
	methods: {
		handleComicReaderReady() {
			this.isComicReaderReady = true;
		},
		handleComicReaderPageChange(newPage) {
			this.page = newPage;
		},
		handleComicReaderLoadMore(loadAfter) {
			const visiblePages = this.pages.filter(page => page.isVisible);
			const numVisiblePages = visiblePages.length;
			const lastPageIndex = numVisiblePages && visiblePages[visiblePages.length - 1].index;
			const firstPageIndex = numVisiblePages && visiblePages[0].index;

			if(this.isLoadingComic ||
				!visiblePages.length ||
				loadAfter && this.isLoadingImagesAfter ||
				!loadAfter && this.isLoadingImagesBefore) return;

			if(loadAfter && lastPageIndex < this.numPages) {
				this.isLoadingImagesAfter = true;
				this.loadMore(lastPageIndex + 1, lastPageIndex + this.numPreloadedImages, false);
			} else if(firstPageIndex > 1) {
				this.isLoadingImagesBefore = true;
				this.loadMore(firstPageIndex - this.numPreloadedImages, firstPageIndex - 1, true);
			}
		},
		loadMore(startPageIndex, endPageIndex, isBefore) {
			const start = Math.max(startPageIndex, 1);
			const end = Math.min(endPageIndex, this.numPages);

			for(let i = start; i <= end; i++) {
				let page = this.pages.find(page => page.index == i);

				if(!page) {
					const newPage = {
						index: i,
						url: "https://picsum.photos/333/500",
						isVisible: false,
						isLoaded: false,
						isBefore: isBefore,
						img: null
					};

					page = this.insertPage(newPage);

					if(isBefore) {
						this.pagesLoadingBefore.push(page);
					} else {
						this.pagesLoadingAfter.push(page);
					}
				}

				if(isBefore) {
					this.pagesLoadedBefore.push(page);
				} else {
					this.pagesLoadedAfter.push(page);
				}
			}

			if(isBefore && !this.pagesLoadingBefore.length) {
				this.onImagesBeforeLoaded();
			}

			if(!isBefore && !this.pagesLoadingAfter.length) {
				this.onImagesAfterLoaded();
			}
		},
		insertPage(page) {
			let j;
			for(j = 0; j < this.pages.length; j++) {
				if(this.pages[j].index > page.index) {
					break;
				}
			}

			this.pages.splice(j, 0, page);

			return page;
		},
		handleComicReaderClick() {
			this.isControlsEnabled = !this.isControlsEnabled;
		},
		handleComicReaderDoubleClick() {
		},
		setDisplayMode(displayMode) {
			this.displayMode = displayMode;
		},
		handleZoomControlChange(value) {
			this.zoomScale = value;
			this.displayMode = "zoom";
		},
		onImagesAfterLoaded() {
			this.pagesLoadedAfter.forEach(page => page.isVisible = true);
			this.pagesLoadedAfter = [];
			this.isLoadingImagesAfter = false;
			this.isLoadingComic = this.isLoadingImagesBefore;
		},
		onImagesBeforeLoaded() {
			this.pagesLoadedBefore.forEach(page => page.isVisible = true);
			this.isLoadingImagesBefore = [];
			this.isLoadingImagesBefore = false;
			this.isLoadingComic = this.isLoadingImagesAfter;
		},
		handlePageLoaded(pageImage) {
			const { pageIndex, width, height } = pageImage;

			const page = this.pages.find(page => page.index == pageIndex);

			if(!page) return;

			page.width = width;
			page.height = height;
			page.isLoaded = true;
			page.img = pageImage.img;

			if(page.isBefore) {
				this.pagesLoadingBefore = this.pagesLoadingBefore.filter(page => page.index != pageIndex);
				this.pagesLoadedBefore.push(page);

				if(!this.pagesLoadingBefore.length) {
					this.onImagesBeforeLoaded();
				}
			} else {
				this.pagesLoadingAfter = this.pagesLoadingAfter.filter(page => page.index != pageIndex);
				this.pagesLoadedAfter.push(page);

				if(!this.pagesLoadingAfter.length) {
					this.onImagesAfterLoaded();
				}
			}
		},
		loadPages(pageIndex) {
			this.isLoadingComic = true;

			if(pageIndex > 1) {
				this.isLoadingImagesBefore = true;
			}

			if(pageIndex < this.numPages) {
				this.isLoadingImagesAfter = true;
			}

			const startPage = Math.max(pageIndex - this.numPreloadedImages, 1);
			const endPage = Math.min(pageIndex + this.numPreloadedImages, this.numPages);

			this.pages.forEach(page => page.isVisible = false);

			for(let i = startPage; i <= endPage; i++) {
				let page = this.pages.find(page => page.index == i);

				if(page) {

					if(page.index >= pageIndex) {
						this.pagesLoadedAfter.push(page);
					} else {
						this.pagesLoadedBefore.push(page);
					}
				} else {
					const newPage = {
						index: i,
						url: "https://picsum.photos/333/500",
						isVisible: false,
						isLoaded: false,
						img: null
					};

					page = this.insertPage(newPage);

					if(page.index >= pageIndex) {
						this.pagesLoadingAfter.push(page);
					} else {
						this.pagesLoadingBefore.push(page);
					}
				}

				page.isBefore = i < pageIndex;
			}

			if(!this.pagesLoadingAfter.length) {
				this.onImagesAfterLoaded();
			}

			if(!this.pagesLoadingBefore.length) {
				this.onImagesBeforeLoaded();
			}
		}
	},
	computed: {
		normalizedZoomScale() {
			return this.zoomScale / 100;
		},
		mainWrapperClassObject() {
			return {
				"main-wrapper--padding-bottom": this.isControlsEnabled
			}
		}
	},
	mounted() {
		this.loadPages(10);
	}
}
</script>

<style>
.options {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	pointer-events: none;
}

.options * {
	pointer-events: auto;
}

</style>
