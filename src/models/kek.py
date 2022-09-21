"""
Define the KEK model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Kek(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Kek model """

    __tablename__ = "kek"

    cid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ciphertext = db.Column(db.LargeBinary(200000))
    tag = db.Column(db.String(300))

    def __init__(self, cid, ciphertext, tag):
        """ Create a new KEK """
        self.cid = cid
        self.ciphertext = ciphertext
        self.tag = tag
