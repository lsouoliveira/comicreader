import traceback
import uuid
from app import models
from app.exceptions import ResourceNotFound, FileNotSupported
from app.main.repository.book_repository import save, save_batch, find, find_by_id
from app.main.readers import ReaderFactory
from app.main.util import file_utils
from app.main.util import thumbnail_utils

ALLOWED_EXTENSIONS = ['cbz']

BOOK_TYPE = {
    'cbz': models.BookType.comic
}

THUMBNAIL_SIZE = (320, 200)
THUMBNAIL_FOLDER = "uploads/thumbnails"

reader_factory = ReaderFactory() 

def save_book(book):
    return save(book)

def add_books(files):
    books_added = []
    errors = []

    for file in files:
        try:
            image_file = files[file]

            filename, file_ext = file_utils.extract_extension(image_file.filename)
            
            if not file_ext in ALLOWED_EXTENSIONS:
                raise FileNotSupported(file)
            
            # Create reader
            reader = reader_factory.create(file_ext) 

            if not reader:
                raise FileNotSupported(file)

            reader.read(image_file.read())

            # Create and save thumbnail 
            image_name, image_data = reader.get_cover()
            _, image_ext = file_utils.extract_extension(image_name)

            thumbnail_name = "{}.{}".format(str(uuid.uuid4()), image_ext)
            thumbnail_path = "{}/{}".format(THUMBNAIL_FOLDER, thumbnail_name)
            thumbnail_utils.save_to(image_data, thumbnail_path, THUMBNAIL_SIZE)

            # Create book entity
            book = models.Book(
                cover_image = thumbnail_name,
                file_id = "",
                num_pages = reader.count_pages(),
                book_type = BOOK_TYPE[file_ext],
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
                    status = models.ProcessStatus.running
                )
            )

            books_added.append(book)
        except FileNotSupported as e:
            traceback.print_exc()
            errors.append(e)
        except Exception as e:
            traceback.print_exc()
            errors.append(FileNotSupported(file))

    # save books
    save_batch(books_added)

    # Create tasks to process each book added
    for book in books_added:
        pass

    return books_added, errors

def get_all_books():
    return find()

def get_book_by_id(id):
    book = find_by_id(id)
    
    if not book:
        raise ResourceNotFound(id)

    return book

def bookmark(id, page):
    book = get_book_by_id(id)

    book.reading_progress.page = page

    return save(book)

def mark_as_read(id, read):
    book = get_book_by_id(id)

    book.reading_progress.read = read

    return save(book)

