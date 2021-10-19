from abc import ABC, abstractmethod
import zipfile
import io
from werkzeug.utils import secure_filename

from app.main.util import file_utils 

ALLOWED_COMIC_IMAGES_EXT = ["png", "jpg", "jpeg"]

class InvalidImageType(Exception):
    def __init__(self):
        super.__init__()

class Reader(ABC):
    @abstractmethod
    def read(self, data: bytearray) -> None:
        pass

    @abstractmethod
    def get_cover(self) -> tuple[str, bytearray]:
        pass

class CbzReader(Reader):
    file = None

    def read(self, data: bytearray) -> None:
        self.file = io.BytesIO(data)

    def get_cover(self) -> tuple[str, bytearray]:
        with zipfile.ZipFile(self.file, 'r') as cbz:
            files = cbz.namelist()
            files.sort()

            cover_filename = files[0]
            _, ext = file_utils.extract_extension(cover_filename) 

            if not ext in ALLOWED_COMIC_IMAGES_EXT:
                raise InvalidImageType()

            with cbz.open(cover_filename) as cover_file:
                return secure_filename(cover_filename), cover_file.read()


class ReaderFactory:
    def create(file_extension: str) -> Reader:
        if file_extension == "cbz":
            return CbzReader()

        return None
