<template> <default-layout>
		<template v-slot:header>
			<logo />
			<v-spacer />
			<v-btn icon @click="handleOpenFileDialog">
				<v-icon>mdi-plus</v-icon>
				</v-btn>
		</template>
		<template v-slot:main>
			<v-container>
				<div class="search-container my-12">
					<v-row no-gutters justify="center">
						<v-col md="5">
							<v-text-field
                filled
                label="Search for a comic name"
								append-icon="mdi-magnify"
								hide-details
                v-model="query"
                @input="handleQueryInput"/>
						</v-col>
					</v-row>
				</div>
				<book-gallery
          :data="books"
          :loading="isFetchingBooks"
          @remove="handleRemoveBook"
          @mark-as-read="handleMarkAsRead"
          @book-unavailable="handleBookUnavailable"
        />
        <p v-if="!books.length && !isFetchingBooks" class="text-center">Empty library</p>
			</v-container>
			<file-upload-dialog
        :show="isFileDialogOpened"
        @close="isFileDialogOpened = false"
        @fileDropped="handleFileDropped"
        :uploadedFiles="uploadedFiles"
      />
      <generic-confirmation-dialog
        title="Remove book?"
        description="are you sure you want to remove this book?"
        confirmButtonValue="Remove"
        :show="showRemoveBookConfirmation"
        @confirm="handleRemoveButtonConfirm"
        @close="showRemoveBookConfirmation = false"
      />
		</template>
	</default-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import DefaultLayout from './../layout/DefaultLayout.vue'
import Logo from './../components/Logo.vue'
import FileUploadDialog from './../components/FileUploadDialog.vue'
import BookGallery from './../components/BookGallery.vue'
import GenericConfirmationDialog from './../components/GenericConfirmationDialog.vue'
import { Book, PROCESS_STATUS } from '../types/book'
import { UploadedFile } from '../types/uploaded_file'

const QUERY_INPUT_TIMEOUT = 500

@Component({
  components: {
    DefaultLayout,
    Logo,
    FileUploadDialog,
    BookGallery,
    GenericConfirmationDialog
  }
})
export default class Home extends Vue {
  isFileDialogOpened = false;
  showRemoveBookConfirmation = false
  bookIdToRemove = null
  query = ''
  queryInputTimeout = null
  isFetchingBooks = true
  isSearchEnabled = true

  mounted() {
    this.getBooks().finally(_ => {
      this.isFetchingBooks = false
    })
  }

  handleOpenFileDialog(): void {
    this.isFileDialogOpened = true
  }

  handleFileDropped(e: Event): void {
    const target = e.target as HTMLInputElement
    const files = target.files

    if(files && files.length) {
      Array.from(files).forEach((fileToUpload) => {
        this.createBook(fileToUpload)
      })
    }
  }

  createBook(file: File): void {
    this.$store.dispatch('books/createBook', file)
  }

  getBooks(query: string) {
    return this.$store.dispatch('books/getBooks', query)
  }

  get theme(): string  {
    return (this.$vuetify.theme.dark) ? 'dark' : 'light'
  }

  get uploadedFiles(): Array<UploadedFile> {
    return this.$store.state['books'].filesUploaded
  }

  get books(): Array<Book> {
    const books = this.$store.state['books'].books
    return books.map((book: any) => {
      const titleMetafield = book.meta.find((meta: any) => meta.key === 'title')
      const title = titleMetafield && titleMetafield.value 
      
      return {
        id: book.id,
        thumbnailUrl: book.cover_image,
        title: title || '',
        readerUrl: this.createReaderUrl(book.id, book.book_type),
        read: book.reading_progress.read,
        status: PROCESS_STATUS.findIndex(status => status === book.book_process.status)
      }
    })
  }

  createReaderUrl(bookId, bookType) {
    switch(bookType) {
      case "BookType.comic":
        return `/readers/comic-reader/${bookId}` 
    }
  }

  handleRemoveBook(bookId) {
    this.bookIdToRemove = bookId
    this.showRemoveBookConfirmation = true
  }

  removeBook(bookId) {
    this.$store.dispatch('books/removeBook', bookId)
  }

  handleRemoveButtonConfirm() {
    this.removeBook(this.bookIdToRemove)
  }

  markAsRead(bookId) {
    this.$store.dispatch('books/markAsRead', bookId)
  }

  handleMarkAsRead(bookId) {
    this.markAsRead(bookId)
  }

  handleBookUnavailable(e) {
    const { status } = e

    switch(status) {
      case 0:
        alert('Book in processing')
        return
    }
  }

  handleQueryInput() {
    if(!this.isSearchEnabled) {
      return
    }

    const query = this.query

    this.getBooks(this.query)
    this.isSearchEnabled = false

    this.queryInputTimeout = setTimeout(() => {
      if(this.query != query) {
        this.getBooks(this.query)
      }

      this.isSearchEnabled = true
    }, QUERY_INPUT_TIMEOUT)
  }

}
</script>

<style lang="scss" scoped>
.gallery {
	display: flex;
	overflow: hidden;
	overflow-x: auto;
}

.gallery > div { 
	margin: 0;
}

.gallery__item {
	max-width: 12.25rem;
}

.books-table-container {
	overflow: hidden;
	overflow-x: auto;
}
</style>
