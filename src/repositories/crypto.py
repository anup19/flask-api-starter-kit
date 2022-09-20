""" Defines the Crypto repository """

from models import Crypto


class CryptoRepository:
    """ The repository for the crypto model """

    @staticmethod
    def get(name):
        """ Query a crypto by name and gslb """
        return Crypto.query.filter_by(name=name).one()

#    def update(self, last_name, first_name, age):
#        """ Update a user's age """
#        user = self.get(last_name, first_name)
#        user.age = age
#
#        return user.save()

    @staticmethod
    def create(name, gslb, version, certificate, key):
        """ Create a new crypto """
        crypto = Crypto(name=name, gslb=gslb, version=version, key=key, certificate=certificate)

        return crypto.save()
