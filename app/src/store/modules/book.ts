import { ActionContext } from 'vuex'
import BookService from '../../services/BookService'
import { UploadedFile, UploadedFileStatus } from '../../types/uploaded_file'
import BookState from '../../types/book_state'
import Pagination from '../../types/pagination'
import Book from '../../types/book'

const state = (): BookState => {
  return {
    filesUploaded: [],
    books: [],
    isFetching: false,
    errors: [],
    pagination: {
      page: 0,
      pagesCount: 0,
      pageSize: 20
    }
  }
}

const getters = {
  getUploadedFiles: (state: BookState) => state.filesUploaded,
  getBooks: (state: BookState) => state.books
}

const actions = {
  createBook(context: ActionContext<BookState, BookState>, file: File): void {
    const uploadedFile = BookService.createUploadedFile(file)

    context.commit('addUploadedFile', uploadedFile)

    BookService.createBook(file, (e: any) => {
      const updatedUploadedFile = {...uploadedFile, uploaded_size: e.loaded}
      context.commit('updateUploadedFile', updatedUploadedFile)
    })
    .then(_ => {
      const updatedUploadedFile = {...uploadedFile, status: UploadedFileStatus.done}
      context.commit('updateUploadedFile', updatedUploadedFile)
    })
    .catch(() => {
      const updatedUploadedFile = {...uploadedFile, status: UploadedFileStatus.error}
      context.commit('updateUploadedFile', updatedUploadedFile)
    })
  },
  getBooks(context: ActionContext<BookState, BookState>, query: string): void {
    const { state } = context
    const pagination = state.pagination

    if(state.isFetching) return

    context.commit('setIsFetching', true)

    BookService.getBooks(query, pagination.page, pagination.pageSize)
      .then(res => {
        const response = res.data
        const { data, pagination } = response

        context.commit('setPagination', {
          page: pagination.page,
          pagesCount: pagination.total_pages,
          pageSize: pagination.items_per_page
        })

        context.commit('setBooks', data)
      })
      .catch(error => {
        const response = error.response
        const data = response.data
        context.commit('setErrors', data.errors)
      })
      .finally(() => context.commit('setIsFetching', false))
  },
  getMoreBooks(context: ActionContext<BookState, BookState>, query: string): void {
    const { state } = context
    const pagination = state.pagination

    if(state.isFetching) return

    context.commit('setIsFetching', true)

    BookService.getBooks(query, pagination.page, pagination.pageSize)
      .then(res => {
        const response = res.data
        const { data, pagination } = response

        context.commit('setPagination', {
          page: pagination.page,
          pagesCount: pagination.total_pages,
          pageSize: pagination.items_per_page
        })

        context.commit('appendBooks', data)
      })
      .catch(error => {
        const response = error.response
        const data = response.data
        context.commit('setErrors', data.errors)
      })
      .finally(() => context.commit('setIsFetching', false))
  }
}

const mutations = {
  addUploadedFile(state: BookState, uploadedFile: UploadedFile): void {
    state.filesUploaded = [...state.filesUploaded, uploadedFile]
  },
  updateUploadedFile(state: BookState, uploadedFile: UploadedFile): void {
    const filesUploaded = state.filesUploaded  
    const uploadedFileFound = filesUploaded.find(fileUploaded => {
      return fileUploaded.id === uploadedFile.id 
    })
    Object.assign(uploadedFileFound, uploadedFile)
  },
  setPagination(state: BookState, pagination: Pagination): void {
    state.pagination = pagination 
  },
  setBooks(state: BookState, books: Array<Book>): void {
    state.books = books 
  },
  appendBooks(state: BookState, books: Array<Book>): void {
    state.books = [...state.books, books]
  },
  setIsFetching(state: BookState, isFetching: boolean): void {
    state.isFetching = isFetching
  },
  setErrors(state: BookState, errors: any): void {
    state.errors = errors
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
