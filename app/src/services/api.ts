import { HttpClient } from './http_client'

export const UnknownError = () => ({
  code: -1
})

export const formatErrorResponse = (errorBody) => {
  const data = errorBody && errorBody.data
  return [
    ...data || [UnknownError]
  ]
}

export class ComicReaderApi extends HttpClient {
  public constructor() {
    super(process.env.VUE_APP_COMIC_READER_API)
  }
}
