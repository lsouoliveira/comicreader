import traceback
import uuid
from app import models
from app.exceptions import ResourceNotFound, FileNotSupported
from app.main.repository.book_repository import save, save_batch, find, find_by_id
from app.main.parsers import Parser, ParserFactory
from app.main.util import file_utils
from app.main.util import thumbnail_utils
from app.models import Book
from app import tasks

THUMBNAIL_SIZE = (320, 200)
THUMBNAIL_FOLDER = "public/thumbnails"
BOOKS_PROCESSING_FOLDER = "uploads/processing"
ALLOWED_EXTENSIONS = ['cbz']

BOOK_TYPE = {
        'cbz': models.BookType.comic
        }

BOOK_FORMAT = {
        'cbz': models.BookFormat.cbz
        }

parser_factory = ParserFactory() 

def save_book(book: Book):
    return save(book)

def add_book(book_file):
    """Return the book successfully persisted."""
    filename, file_ext = file_utils.extract_extension_and_secure(book_file.filename)

    if not file_ext in ALLOWED_EXTENSIONS:
        raise FileNotSupported(book_file.filename)

    book_format = BOOK_FORMAT[file_ext]
    book_data = book_file.read()

    parser = create_parser(book_data, book_format, book_file)
    thumbnail_name = save_thumbnail(book_data, parser, file_ext)
    file_id = save_bookfile_to_directory(book_data, file_ext)

    book = models.Book(
        cover_image = thumbnail_name,
        num_pages = parser.count_pages(),
        book_type = BOOK_TYPE[file_ext],
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
            file_id = file_id 
        )
    )

    save(book)
    tasks.extract_archive.apply_async(args=[book.id])

    return book

def save_bookfile_to_directory(book_data, file_extension):
    file_id = "{}.{}".format(str(uuid.uuid4()), file_extension)

    with open("{}/{}".format(BOOKS_PROCESSING_FOLDER, file_id), 'wb') as f:
        f.write(book_data)

    return file_id

def save_thumbnail(book_data, parser, file_extension):
    image_name, image_data = parser.get_cover()
    thumbnail_name = create_thumbnail(image_data, image_name)

    return thumbnail_name

def create_parser(book_data, book_format, book_file):
    parser = parser_factory.create(book_format) 

    if not parser:
        raise FileNotSupported(book_file.filename)

    parser.read(book_data)

    return parser

def create_thumbnail(data: bytes, image_name: str) -> str:
    """Return a file path to a thumbnail created."""
    _, image_ext = file_utils.extract_extension(image_name)

    thumbnail_name = "{}.{}".format(str(uuid.uuid4()), image_ext)
    thumbnail_path = "{}/{}".format(THUMBNAIL_FOLDER, thumbnail_name)

    thumbnail_utils.save_to(data, thumbnail_path, THUMBNAIL_SIZE)

    return thumbnail_name


def get_all_books():
    return find()

def get_book_by_id(id: int):
    book = find_by_id(id)

    if not book:
        raise ResourceNotFound(id)

    return book

def bookmark(id: int, page: int):
    book = get_book_by_id(id)

    book.reading_progress.page = page

    return save(book)

def mark_as_read(id: int, read: bool):
    book = get_book_by_id(id)

    book.reading_progress.read = read

    return save(book)

