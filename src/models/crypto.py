"""
Define the Crypto model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Crypto(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Crypto model """

    __tablename__ = "crypto"

    name = db.Column(db.String(300), primary_key=True)
    gslb = db.Column(db.String(300))
    version = db.Column(db.String(300))
    certificate = db.Column(db.String(100000))
    key = db.Column(db.String(100000))

    def __init__(self, name, gslb, version, certificate, key):
        """ Create a new Crypto """
        self.name = name
        self.gslb = gslb
        self.version = version
        self.certificate = certificate
        self.key = key
