"""
Defines the blueprint for the crypto
"""
from flask import Blueprint
from flask_restful import Api

from resources import CryptoResource

CRYPTO_BLUEPRINT = Blueprint("crypto", __name__)
Api(CRYPTO_BLUEPRINT).add_resource(
    CryptoResource, "/crypto/<string:name>"
)
