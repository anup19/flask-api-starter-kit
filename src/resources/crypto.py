"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CryptoRepository
from util import parse_params


class CryptoResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/crypto/GET.yml")
    def get(name):
        """ Return a crypto object information based on his name """
        crypto = CryptoRepository.get(name=name)
        return jsonify({"crypto": crypto.json})

    @staticmethod
    @parse_params(
        Argument("version", location="json", required=True, help="The version of the crypto"),
        Argument("certificate", location="json", required=True, help="The certificate of the crypto"),
        Argument("key", location="json", required=True, help="The key of the crypto"),
        Argument("gslb", location="json", required=True, help="The key of the crypto")
    )
    @swag_from("../swagger/crypto/POST.yml")
    def post(name, gslb, version, certificate, key):
        """ Create a crypto secret based on the sent information """
        crypto = CryptoRepository.create(
            name=name, gslb=gslb, version=version, key=key, certificate=certificate
        )
        return jsonify({"crypto": crypto.json})

#    @staticmethod
#    @parse_params(
#        Argument("age", location="json", required=True, help="The age of the user.")
#    )
#    @swag_from("../swagger/user/PUT.yml")
#    def put(last_name, first_name, age):
#        """ Update an user based on the sent information """
#        repository = UserRepository()
#        user = repository.update(last_name=last_name, first_name=first_name, age=age)
#        return jsonify({"user": user.json})
