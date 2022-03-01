from app.exceptions import ResourceNotFound, FileNotSupported
from app.main.service import book_service, archive_service
from app.main.parsers import Parser, ParserFactory
from app.main.util import file_utils
from app.main.util import thumbnail_utils
from app.models import Book
from app import models
from app import tasks
import traceback
import uuid

ALLOWED_EXTENSIONS = ['cbz']

BOOK_TYPE = {
        'cbz': models.BookType.comic
        }

BOOK_FORMAT = {
        'cbz': models.BookFormat.cbz
        }

parser_factory = ParserFactory() 

def add_book(book_file):
    """Return the book successfully persisted."""
    filename, file_extension = file_utils.extract_extension(book_file.filename)

    if not file_extension in ALLOWED_EXTENSIONS:
        raise FileNotSupported(book_file.filename)

    book_format = BOOK_FORMAT[file_extension]
    file_data = book_file.read()

    parser = create_parser(file_data, book_format, book_file)
    image_name, image_data = parser.get_cover()

    thumbnail_filename = archive_service.save_thumbnail(image_data, image_name) 
    book_file_id = archive_service.save_book_for_processing(
        file_data, file_extension
    )

    book = models.Book(
            cover_image = thumbnail_filename,
            num_pages = parser.count_pages(),
            book_type = BOOK_TYPE[file_extension],
            book_format = book_format,
            reading_progress = models.ReadingProgress(
                page=1,
                read=False
                ),
            meta = [
                models.Metadata(
                    key = "title",
                    value = filename,
                    data_type = models.DataType.string
                    )
                ],
            book_process = models.BookProcess(
                error_code = 0,
                status = models.ProcessStatus.running,
                file_id = book_file_id 
                )
            )

    book_service.save(book)
    tasks.extract_archive.apply_async(args=[book.id])

    return book

def create_parser(file_data, book_format, book_file):
    parser = parser_factory.create(book_format) 

    if not parser:
        raise FileNotSupported(book_file.filename)

    parser.read(file_data)

    return parser
