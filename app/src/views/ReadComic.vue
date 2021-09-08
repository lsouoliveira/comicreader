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
					:remain-images-trigger="remainImagesTrigger"
					:pages="pages"
					@page-load="handlePageLoaded"
					/>
			</div>
			<loading :show="isLoadingComic" />
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

	const pages = [
			"http://localhost:8080/onepiece_vol1_cover.jpg",
			"http://localhost:8080/onepiece_vol1_cover.jpg",
			"http://localhost:8080/onepiece_vol1_cover.jpg",
			"http://localhost:8080/onepiece_vol1_cover.jpg",
			"http://localhost:8080/onepiece_vol1_cover.jpg"
		];

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
							page: 1,
							numPages: 5,
							remainImagesTrigger: 5,
							numPreloadedImages: 5,
							pages: [],
							pagesLoadingBefore: [],
							pagesLoadingAfter: [],
							pagesLoadedBefore: [],
							pagesLoadedAfter: [],
							isLoadingImagesBefore: false,
							isLoadingImagesAfter: false
						};
				},
			methods: {
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
							this.isLoadingImagesBefore = false;
						},
					onImagesBeforeLoaded() {
							this.isLoadingImagesBefore = false;
							this.pagesLoadedBefore.forEach(page => page.isVisible = true);
						},
					handlePageLoaded(pageIndex) {
							const page = this.pages.find(page => page.index == pageIndex);

							if(!page) return;

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
							this.isLoadingImagesBefore = this.isLoadingImagesAfter = true;

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
														url: pages[i - 1],
														isVisible: false
													};

												let minIndex = 0;
												for(let j = 0; j < this.pages.length; j++) {
														if(this.pages[j].index + 1 > i) {
																break;
															}

														minIndex = j;
													}

												this.pages.splice(minIndex + 1, 0, newPage);

												page = newPage;

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
						},
					isLoadingComic() {
							return this.isLoadingImagesBefore && this.isLoadingImagesAfter;
						}
				},
			mounted() {
					this.loadPages(1);
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
