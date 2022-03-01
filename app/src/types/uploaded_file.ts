export enum UploadedFileStatus {
  in_progress,
  error,
  done
}

export interface UploadedFile {
  id: number,
  name: string,
  uploaded_size: number,
  size: number,
  status: UploadedFileStatus
}
