import { ComicReaderApi } from "./api";
import { GetBooksResponse, GetBookResponse } from '../types/api'
import { UploadedFile, UploadedFileStatus } from '../types/uploaded_file'

const FILE_KEY = 'file'

class BookApi extends ComicReaderApi {
	createBook(file: File, onUploadProgress: (e: Event) => void): Promise<any> {
    const formData = this.createFileUploadFormData(file)
    const config   = this.createFileUploadConfig(onUploadProgress) 

		return this.instance.post<GetBookResponse>(
			"/books/",
			formData,
      config
		)
	}

  getBooks(query: string, page: number, pageSize: number) {
    const config = {
      params: {
        query
      }
    }
    return this.instance.get<GetBooksResponse>("/books", config)
  }

  getBook(bookId: string) {
    return this.instance.get<GetBookResponse>(`/books/${bookId}`)
  }

  deleteBook(bookId: string) {
    return this.instance.delete<void>(`/books/${bookId}`)
  }

  bookmark(id: string, bookmarkData: any) {
    const { page, percent } = bookmarkData

    return this.instance.put(`/books/${id}/bookmark`, { page, percent })
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

export default new BookApi();
