from typing import Optional, Tuple
from os import listdir, path
import mimetypes
import uuid

from app.main.parsers import CbzParser, Parser, ParserFactory
from app.exceptions import ResourceNotFound
from app.main.util import thumbnail_utils
from app.main.util import file_utils
from app.models import BookFormat

BOOKS_EXTRACTED_FOLDER = "uploads/books"
BOOKS_PROCESSING_FOLDER = "uploads/processing"
THUMBNAIL_FOLDER = "public/images"
THUMBNAIL_SIZE = (200, 320)

def extract_archive(path: str, filename: str, book_format: BookFormat) -> None:
    """Extract a book file to target folder."""
    parser_factory = ParserFactory()
    parser = parser_factory.create(book_format)

    book_extracted_path = "{}/{}".format(BOOKS_EXTRACTED_FOLDER, filename)

    if parser is None:
        raise Exception()

    with open(path, "rb") as f:
        parser.read(f.read())

        parser.extract_to(book_extracted_path)

def get_comic_page(book_id: int, page_number: int) -> str:
    """Return path to image data from target comic folder."""
    book_folder = path.join(BOOKS_EXTRACTED_FOLDER, str(book_id))
    
    page_index = page_number - 1

    if path.exists(book_folder):
        pages = [f for f in listdir(book_folder)]
        pages.sort(key=lambda x: int(x.split('.')[0]))

        if page_number < 1 or page_number > len(pages):
            raise ResourceNotFound(page_number)
        
        return "../" + path.join(book_folder, pages[page_index])

    raise ResourceNotFound(page_number)

def save_thumbnail(data, image_name):
    """Return a file path to a thumbnail created."""
    _, image_ext = file_utils.extract_extension(image_name)

    thumbnail_name = "{}.{}".format(str(uuid.uuid4()), image_ext)
    thumbnail_path = "{}/{}".format(THUMBNAIL_FOLDER, thumbnail_name)

    thumbnail_utils.save_to(data, thumbnail_path, THUMBNAIL_SIZE)

    return thumbnail_name

def save_book_for_processing(file_data, file_extension):
    file_id = "{}.{}".format(str(uuid.uuid4()), file_extension)

    with open("{}/{}".format(BOOKS_PROCESSING_FOLDER, file_id), 'wb') as f:
        f.write(file_data)

    return file_id
