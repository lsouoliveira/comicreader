import unittest

from app.main import db
import json
from app.test.base import BaseTestCase
from app.main.model.book import Book, BookType
from app.main.model.readingprogress import ReadingProgress 

def create_book():
    book = Book(
        cover_image = "image.jpg",
        file_id = "file_id",
        num_pages = 100,
        book_type = BookType.comic,
        reading_progress = ReadingProgress(
            page=1,
            read=False
        )
    )
    db.session.add(book)
    db.session.commit()

    return book

class TestBookController(BaseTestCase):
    def test_get_books(self):
        with self.client:
            create_book()

            response = self.client.get('/v1/books/')

            data = json.loads(response.data.decode())

            self.assertTrue('data' in data)
            self.assertTrue('pagination' in data)
            self.assertEqual(len(data['data']), 1)
            self.assertEqual(response.status_code, 200)

    def test_get_book_by_id(self):
        with self.client:
            book_created = create_book()

            response = self.client.get('/v1/books/{}'.format(book_created.id))

            data = json.loads(response.data.decode())

            self.assertTrue('data' in data)
            self.assertEqual(data['data']['id'], book_created.id)
            self.assertEqual(response.status_code, 200)

    def test_bookmark(self):
        with self.client:
            book_created = create_book()

            new_page = 2

            response = self.client.put(
                    '/v1/books/{}/bookmark'.format(book_created.id),
                    data=json.dumps({'page': new_page}),
                    content_type='application/json')
            

            data = json.loads(response.data.decode())

    def test_bookmark_without_body(self):
        with self.client:
            book_created = create_book()

            new_page = 2

            response = self.client.put('/v1/books/{}/bookmark'.format(book_created.id))

            data = json.loads(response.data.decode())

            self.assertTrue('errors' in data)
            self.assertEqual(response.status_code, 400)

    def test_mask_as_read(self):
        with self.client:
            book_created = create_book()

            response = self.client.put('/v1/books/{}/mark-as-read'.format(book_created.id))

            data = json.loads(response.data.decode())

            self.assertTrue(data['data']['reading_progress']['read'], True)

    def test_mark_as_unread(self):
        with self.client:
            book_created = create_book()

            response = self.client.put('/v1/books/{}/mark-as-unread'.format(book_created.id))

            data = json.loads(response.data.decode())

            self.assertEqual(data['data']['reading_progress']['read'], False)

if __name__ == '__main__':
    unittest.main()

