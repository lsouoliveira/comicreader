from os import listdir, path
from typing import Optional, Tuple
import mimetypes
from app.models import BookFormat
from app.main.parsers import CbzParser, Parser, ParserFactory
from app.exceptions import ResourceNotFound

BOOKS_EXTRACTED_FOLDER = "uploads/books"

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

        if page_number < 1 or page_number > len(pages):
            raise ResourceNotFound(page_number)
        
        return "../" + path.join(book_folder, pages[page_index])

    raise ResourceNotFound(page_number)
