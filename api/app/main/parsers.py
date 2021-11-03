from abc import ABC, abstractmethod
import zipfile
import io
from typing import Optional

from werkzeug.utils import secure_filename

from app.main.util import file_utils 
from app.models import BookFormat

ALLOWED_COMIC_IMAGES_EXT = ["png", "jpg", "jpeg"]

class InvalidImageType(Exception):
    def __init__(self):
        super.__init__()

class Parser(ABC):
    @abstractmethod
    def read(self, data: bytes) -> None:
        pass

    @abstractmethod
    def get_cover(self) -> tuple[str, bytes]:
        pass

    @abstractmethod
    def count_pages(self) -> int:
        pass

    @abstractmethod
    def extract_to(self, path: str) -> None:
        pass

class CbzParser(Parser):
    file = None

    def read(self, data: bytes) -> None:
        self.file = io.BytesIO(data)

    def get_cover(self) -> tuple[str, bytes]:
        with zipfile.ZipFile(self.file, 'r') as cbz:
            files = cbz.namelist()
            files.sort()

            cover_filename = files[0]
            _, ext = file_utils.extract_extension(cover_filename) 

            if not ext in ALLOWED_COMIC_IMAGES_EXT:
                raise InvalidImageType()

            with cbz.open(cover_filename) as cover_file:
                return secure_filename(cover_filename), cover_file.read()

    def count_pages(self):
        with zipfile.ZipFile(self.file, 'r') as cbz:
            return len(cbz.namelist())

    def extract_to(self, path: str) -> None:
        with zipfile.ZipFile(self.file, 'r') as cbz:
            cbz.extractall(path)



class ParserFactory:
    def create(self, book_format: BookFormat) -> Optional[Parser]:
        if book_format == BookFormat.cbz:
            return CbzParser()

        return None
