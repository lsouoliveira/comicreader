import os
import traceback
from . import celery
from flask import current_app
from app.main.service import book_service
from app.main.service import archive_service
from app.models import BookFormat, ProcessStatus 


@celery.task(name="app.tasks.extract_archive")
def extract_archive(book_id: int) -> None:
    """Extract the book archive (cbz, cbr, epub, ...) to the 'books folder'."""
    book = None

    try:
        book = book_service.get_book_by_id(book_id)
    except:
        return

    book_path = "{}/{}".format(book_service.BOOKS_PROCESSING_FOLDER,
            book.book_process.file_id) 

    try:
        archive_service.extract_archive(book_path, str(book_id), book.book_format)

        book.book_process.status = ProcessStatus.finished
    except:
        traceback.print_exc()
        book.book_process.status = ProcessStatus.error
    finally:
        os.remove(book_path)
        book_service.save(book)
