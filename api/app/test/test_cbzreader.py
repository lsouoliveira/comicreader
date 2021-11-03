import unittest

import datetime

from app import db
from app.main.parsers import CbzParser

from app.test.base import BaseTestCase

def load_sample():
    file_path = "data/sample.cbz"

    with open(file_path, "rb") as f:
        return f.read()

class TestCbzReader(BaseTestCase):
    def test_get_cover(self):
        parser = CbzParser()
        sample = load_sample()

        parser.read(sample)
        image_name, data = parser.get_cover()

        self.assertEqual(image_name, "1.jpg")

if __name__ == '__main__':
    unittest.main()

