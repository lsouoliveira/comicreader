import { ActionContext } from 'vuex'
import { UnknownError, formatErrorResponse } from '../../services/api'
import BookApi from '../../services/book_api'
import { UploadedFile, UploadedFileStatus } from '../../types/uploaded_file'
import BookState from '../../types/book_state'
import { Pagination } from '../../types/pagination'
import { Book } from '../../types/book'

const state = (): BookState => {
  return {
    filesUploaded: [],
    books: [],
    isFetching: false,
    errors: [],
    pagination: {
      page: 0,
      total_pages: 0,
      items_per_page: 20
    },
    query: '',
    isBookmarking: false
  }
}

const setErrors = (context, errorResponse) => {
  const errors = formatErrorResponse(errorResponse)
  context.commit('setErrors', errors)
}

const getters = {
  getUploadedFiles: (state: BookState) => state.filesUploaded,
    getBooks: (state: BookState) => state.books
}

const actions = {
  async createBook(context: ActionContext<BookState, BookState>, file: File) {
    const { state } = context
    const uploadedFile = BookApi.createUploadedFile(file)

    context.commit('addUploadedFile', uploadedFile)

    try {
      const response = await BookApi.createBook(file, (e: any) => {
        const updatedUploadedFile = {...uploadedFile, uploaded_size: e.loaded}
        context.commit('updateUploadedFile', updatedUploadedFile)
      })
      const { data } = response.data
      const updatedUploadedFile = {...uploadedFile, status: UploadedFileStatus.done}

      if(!state.query.length) {
        context.commit('appendBooks', [data])
      }

      context.commit('updateUploadedFile', updatedUploadedFile)
    } catch(errorResponse) {
      const updatedUploadedFile = {...uploadedFile, status: UploadedFileStatus.error}
      context.commit('updateUploadedFile', updatedUploadedFile)
    }
  },
  async getBooks(context: ActionContext<BookState, BookState>, query: string) {
    const { state } = context
    const { page, items_per_page } = state.pagination

    if(state.isFetching) return

      context.commit('setIsFetching', true)

      try {
        const response = await BookApi.getBooks(query, page, items_per_page)
        const { data, pagination } = response.data

        context.commit('setPagination', pagination) 
        context.commit('setBooks', data)
      } catch(res) {
        setErrors(context, res)
      }

      context.commit('setIsFetching', false)
  },
  async getMoreBooks(context: ActionContext<BookState, BookState>, query: string) {
    const { state } = context
    const { page, items_per_page } = state.pagination

    if(state.isFetching) return

      context.commit('setIsFetching', true)

      try {
        const response = await BookApi.getBooks(query, page, items_per_page)
        const { data, pagination } = response.data

        context.commit('setPagination', pagination) 
        context.commit('appendBooks', data)
      } catch(res) {
        setErrors(context, res)
      }

      context.commit('setIsFetching', false)
  },
  removeBook(context: ActionContext<BookState, BookState>, bookId: string): void {
    const response = BookApi.deleteBook(bookId)
    context.commit('removeBook', bookId)
  },
  markAsRead(context: ActionContext<BookState, BookState>, bookId: string): void {
    context.commit('markAsRead', bookId)
  },
  async bookmark(context: ActionContext<BookState, BookState>, payload) {
    const { bookId, bookmarkData } = payload
    context.commit('setIsBookmarking', true)
    await BookApi.bookmark(bookId, bookmarkData)
    context.commit('setIsBookmarking', false)
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
  appendBooks(state: BookState, books: Book[]): void {
    state.books = [...state.books, ...books]
  },
  setIsFetching(state: BookState, isFetching: boolean): void {
    state.isFetching = isFetching
  },
  setIsBookmarking(state: BookState, isBookmarking: boolean): void {
    state.isBookmarking = isBookmarking
  },
  setErrors(state: BookState, errors: any): void {
    state.errors = errors
  },
  removeBook(state: BookState, bookId: string): void {
    state.books = state.books.filter(book => book.id !== bookId)
  },
  markAsRead(state: BookState, bookId: string): void {
    const book = state.books.find(book => book.id === bookId)

    if(book) {
      book.reading_progress.read = true
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
