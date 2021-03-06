import os
import traceback
from . import celery
from flask import current_app
from app.main.service import book_service
from app.main.service import archive_service
from app.models import ProcessStatus 


@celery.task(name="app.tasks.extract_archive")
def extract_archive(book_id: int):
    """Extract the book archive (cbz, cbr, epub, ...) to the 'books folder'."""
    book = None

    try:
        book = book_service.get_book_by_id(book_id)
    except:
        traceback.print_exc()
        return False

    book_path = "{}/{}".format(archive_service.BOOKS_PROCESSING_FOLDER,
            book.book_process.file_id) 

    try:
        archive_service.extract_archive(book_path, str(book_id), book.book_format)

        book.book_process.status = ProcessStatus.finished

        return True
    except:
        traceback.print_exc()
        book.book_process.status = ProcessStatus.error

        return False
    finally:
        os.remove(book_path)
        book_service.save(book)
