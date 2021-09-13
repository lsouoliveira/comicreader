from .. import db
import datetime
from enum import Enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM

class DataType(Enum):
    string = 1

class Metadata(db.Model):
    """ Metadata Model for storing book metadata """
    __tablename__ = "metadata"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(512), nullable=False)
    value = db.Column(db.String(512), nullable=False)
    data_type = db.Column("data_type", ENUM(DataType, name="datatype_enum"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now(),
            server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Metadata '{}'>".format(self.id)
