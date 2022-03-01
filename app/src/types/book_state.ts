import { UploadedFile } from './uploaded_file'
import Book from './book'
import Pagination from './pagination'

export default interface BookState {
  filesUploaded: UploadedFile[],
  books: Array<Book>,
  isFetching: boolean,
  errors: any,
  pagination: Pagination
}
