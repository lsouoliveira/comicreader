from abc import ABC, abstractmethod
import zipfile
import io
import os
from typing import Optional, Tuple, IO
from PIL import Image

from app.main.util import file_utils 
from app.models import BookFormat

ALLOWED_COMIC_IMAGES_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif"]


class InvalidImageType(Exception):
    def __init__(self):
        pass

class InvalidFileFormat(Exception):
    def __init__(self):
        pass

class Parser(ABC):
    data: IO[bytes]

    @abstractmethod
    def get_cover(self) -> Tuple[str, bytes]:
        pass

    def parse(self, data: bytes) -> None:
        self.data = io.BytesIO(data)

        if not self.is_valid():
            raise InvalidFileFormat()

    @abstractmethod
    def count_pages(self) -> int:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def extract_to(self, path: str) -> None:
        pass

class CbzParser(Parser):

    def get_cover(self) -> Tuple[str, bytes]:
        with zipfile.ZipFile(self.data, 'r') as _:
            cover_file = self.get_first_image()

            if not cover_file:
                raise InvalidImageType()

            return cover_file.name, cover_file.read_bytes()

    def is_valid(self):
        return True

    def count_pages(self):
        return len(self._get_valid_images_paths())

    def _iter_files(self):
        with zipfile.ZipFile(self.data, 'r') as file:
            root_path = zipfile.Path(file)
            members = [root_path]

            while len(members) > 0:
                member = members.pop(0)

                if member.is_file():
                    yield member
                    continue

                new_members = sorted(list(member.iterdir()), key=lambda x: x.name)
                members += new_members

    def extract_to(self, path: str) -> None:
        file_index = 1

        if not os.path.exists(path):
            os.mkdir(path)
        
        for image_path in self._get_valid_images_paths():
            output_path = '{}/{}.{}'.format(path, str(file_index), 'webp')

            with Image.open(io.BytesIO(image_path.read_bytes())) as im:
                im.save(output_path)

            file_index += 1

    def _get_valid_images_paths(self):
        return list(filter(lambda x: self._is_image_valid(x.name), self._iter_files()))

    def _is_image_valid(self, filename):
        _, file_extension = file_utils.extract_extension(filename)
        return file_extension in ALLOWED_COMIC_IMAGES_EXTENSIONS

    def get_first_image(self):
        return (self._get_valid_images_paths() or [None])[0]


class ParserFactory:
    def create(self, book_format: BookFormat) -> Optional[Parser]:
        if book_format == BookFormat.cbz:
            return CbzParser()

        return None
