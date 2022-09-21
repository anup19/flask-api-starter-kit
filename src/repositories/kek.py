""" Defines the KEK repository """

from models import Kek


class KekRepository:
    """ The repository for the KEK model """

    @staticmethod
    def get(cid):
        """ Query a kek by cid"""
        return Kek.query.filter_by(cid=cid).one_or_none()

#    def update(self, last_name, first_name, age):
#        """ Update a user's age """
#        user = self.get(last_name, first_name)
#        user.age = age
#
#        return user.save()

    @staticmethod
    def create(cid, ciphertext, tag):
        """ Create a new kek """
        kek = Kek(cid=cid, ciphertext=ciphertext, tag=tag)

        return kek.save()
