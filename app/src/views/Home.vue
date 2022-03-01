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
								solo
								placeholder="Type a comic name"
								append-icon="mdi-magnify"
								hide-details/>
						</v-col>
					</v-row>
				</div>
				<book-gallery :data="books" />
			</v-container>
			<file-upload-dialog
        :show="isFileDialogOpened"
        @close="isFileDialogOpened = false"
        @fileDropped="handleFileDropped"
        :uploadedFiles="uploadedFiles"
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
import Book from '../types/book'
import { UploadedFile } from '../types/uploaded_file'

@Component({
  components: {
    DefaultLayout,
    Logo,
    FileUploadDialog,
    BookGallery
  }
})
export default class Home extends Vue {
  isFileDialogOpened = false;

  mounted() {
    this.getBooks("")
  }

  handleOpenFileDialog(): void {
    this.isFileDialogOpened = true
  }

  handleFileDropped(e: Event): void {
    const target = e.target as HTMLInputElement
    const files = target.files

    if(files && files.length) {
      const fileToUpload = files[0]

      this.createBook(fileToUpload)
    }
  }

  createBook(file: File): void {
    this.$store.dispatch('books/createBook', file)
  }

  getBooks(query: string): void {
    this.$store.dispatch('books/getBooks', query)
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
        reader_url: this.createReaderUrl(book.id, book.book_type) 
      }
    })
  }

  createReaderUrl(bookId, bookType) {
    switch(bookType) {
      case "BookType.comic":
        return `/readers/comic-reader/${bookId}` 
    }
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
