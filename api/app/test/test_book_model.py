import unittest

import datetime

from app import db
from app.models import Book, BookType
from app.models import Metadata, DataType
from app.models import BookProcess, ProcessStatus
from app.models import ReadingProgress

from app.test.base import BaseTestCase


class TestBookModel(BaseTestCase):

    def test_save(self):
        book = Book(
            cover_image = "image.jpg",
            file_id = "file_id",
            num_pages = 100,
            book_type = BookType.comic,
        )
        db.session.add(book)
        db.session.commit()

    def test_save_with_children(self):
        book = Book(
            cover_image = "image.jpg",
            file_id = "file_id",
            num_pages = 100,
            book_type = BookType.comic,
            meta = [
                    Metadata(
                        key = "title",
                        value = "Test",
                        data_type = DataType.string
                    )
                ],
            book_process = BookProcess(
                    status = ProcessStatus.finished,
                    error_code = 0
                 ),
            reading_progress = ReadingProgress(
                    page = 0,
                    read = False
                )
        )
        db.session.add(book)
        db.session.commit()

if __name__ == '__main__':
    unittest.main()

