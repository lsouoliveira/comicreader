import api from "./api";
import Book from "../types/book";
import { UploadedFile, UploadedFileStatus } from '../types/uploaded_file'

const FILE_KEY = 'file'

/** BookService has all api calls related to book's domain. */
class BookService {
	createBook(file: File, onUploadProgress: (e: Event) => void): Promise<any> {
    const formData = this.createFileUploadFormData(file)
    const config   = this.createFileUploadConfig(onUploadProgress) 

		return api.post(
			"/books/",
			formData,
      config
		)
	}

  getBooks(query: string, page: number, pageSize: number): Promise<any> {
    const config = {
      params: {
        query
      }
    }
    return api.get("/books", config)
  }

  getBook(bookId: string): Promise<any> {
    return api.get(`/books/${bookId}`)
  }

  bookmark(id: string, bookmarkData: any): Promise<any> {
    const { page, percent } = bookmarkData

    return api.put(`/books/${id}/bookmark`, { page, percent })
  }

  createUploadedFile(file: File): UploadedFile {
    return {
      id: new Date().getTime(),
      name: file.name,
      uploaded_size: 0,
      size: file.size,
      status: UploadedFileStatus.in_progress
    }
  }

  private createFileUploadFormData(file: File): FormData {
    const formData = new FormData()
    formData.append(FILE_KEY, file)

    return formData
  }

  private createFileUploadConfig(onUploadProgress: (e: Event) => void): any {
    return {
      headers: {
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress: onUploadProgress 
    }
  }
}

export default new BookService();
