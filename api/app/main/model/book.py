from .. import db
import datetime
from enum import Enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM

class BookType(Enum):
    comic = 1

class Book(db.Model):
    """ Book Model for storing book related details """
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cover_image = db.Column(db.String(512), nullable=False)
    file_id = db.Column(db.String(512), unique=True, nullable=False)
    num_pages = db.Column(db.Integer, nullable=False, default=0)
    book_type = db.Column("book_type", ENUM(BookType, name="booktype_enum"), nullable=False)
    meta = db.relationship("Metadata")
    book_process = db.relationship("BookProcess", uselist=False)
    reading_progress = db.relationship("ReadingProgress", uselist=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Book '{}'>".format(self.id)
