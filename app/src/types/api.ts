import { Book } from './book'
import { Pagination } from './pagination'

export interface ErrorResponse {
  data?: any
}

export interface ApiResponse<Type> {
  data?: Type
}

export interface GetBooksResponse {
  data: Book[],
  pagination: Pagination 
}

export interface GetBookResponse {
  data: Book
}
