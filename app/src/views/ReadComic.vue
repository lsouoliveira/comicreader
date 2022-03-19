<template>
	<v-app>
		<v-app-bar app dark v-if="isControlsEnabled">
			<v-toolbar-title class="title">{{this.book && this.book.title}}</v-toolbar-title>
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
					<v-list-item link @click="setDisplayMode('fit-height')"> Adjust to height
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
					:percent="percent"
					:num-pages="numPages"
					:remain-images-to-trigger="remainImagesToTrigger"
					:pages="pages"
					:is-loading-images-before="isLoadingImagesBefore"
					:is-loading-images-after="isLoadingImagesAfter"
					:is-loading-comic="isLoadingComic"
					@scroll-change="handleScrollChange"
					@page-load="handlePageLoaded"
					@page-change="handleComicReaderPageChange"
					@load-more="handleComicReaderLoadMore"
					@ready="handleComicReaderReady"
				/>
			</div>
			<loading :show="isLoadingComic || !isComicReaderReady" />
      <div class="sync-loading">
        <v-progress-circular
          indeterminate
          size="16"
          width="2"
          color="dark"
          v-show="isBookmarking"/>
          <v-icon size="16" color="dark" v-show="!isBookmarking">mdi-check</v-icon>
      </div>
		</v-main>
		<v-app-bar
			fixed
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
import BookApi from './../services/book_api'

const API_URL = process.env.VUE_APP_COMIC_READER_API

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
			percent: 0,
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
			isComicReaderReady: false,
      comicBookId: null,
      book: null,
      bookmarkTimeout: null,
      bookmarkInterval: 500
		};
	},
	methods: {
		handleComicReaderReady() {
			this.isComicReaderReady = true;
		},
		handleScrollChange(e) {
      if(this.bookmarkTimeout) {
        clearTimeout(this.bookmarkTimeout)
      }

      this.bookmarkTimeout = setTimeout(() => {
        this.$store.dispatch('books/bookmark', { bookId: this.book.id, bookmarkData: { page: this.page, percent: e.percent } })
      }, this.bookmarkInterval);
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

			if(loadAfter && lastPageIndex <= this.numPages) {
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
						url: this.createPageUrl(i),
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
      return
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

			if(pageIndex <= this.numPages) {
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
						url: this.createPageUrl(i),
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
		},
    async loadBook(bookId) {
      BookApi.getBook(bookId)
        .then(res => {
          const data = res.data
          const book = data.data 
          const titleMetafield = book.meta.find(meta => meta.key === 'title')
          const bookTitle = titleMetafield.value || ''
          this.book = {
            id: book.id,
            title: bookTitle
          }
          this.numPages = book.num_pages
          this.page = book.reading_progress.page
          this.percent = book.reading_progress.percent

          this.loadPages(this.page)
        })
        .catch(_ => {
          alert('book not found')
        })
    },
    createPageUrl(pageIndex) {
      return `${API_URL}/books/${this.book.id}/readers/comic/pages/${pageIndex}`
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
    isBookmarking() {
      return this.$store.state['books'].isBookmarking
    }
  },
  watch: {
    pages() {
      for(let i = 1; i < this.pages.length; i++) {
        if(this.pages[i].index < this.pages[i - 1].index) {
          alert('wrong order')
        }
      }
    }
  },
	mounted() {
    this.comicBookId = this.$route.params.id
    this.loadBook(this.comicBookId)
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

.sync-loading {
  position: fixed;
  top: 8px;
  right: 16px;
}
</style>
