export const PROCESS_STATUS = ['running', 'finished', 'error']

interface ReadingProgress {
  read: boolean
}

interface BookProcess {
  status: string
}

export interface Book {
  id: string,
  reading_progress: ReadingProgress,
  book_process: BookProcess
}
