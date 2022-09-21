import boto3
import json
import base64

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import KekRepository
from util import parse_params

from cryptography.fernet import Fernet


class KMSHandler(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(KMSHandler, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        print("INIT -- hh")
        self.kms_client = boto3.client("kms")
        self.kek = ''

    # Create data key
    def generate_kek(self):
        print("generating")
        response = self.kms_client.generate_data_key(KeyId='alias/foo', KeySpec='AES_256')
        return response

    def decrypt_crypto_secret(self, encrypted_secret):
        f = Fernet(self.kek)
        decrypted_secret = f.decrypt(encrypted_secret)

        print(decrypted_secret.decode())
        return decrypted_secret.decode()

    def encrypt_crypto_secret(self, secret):

        encoded_secret = secret.encode()
        f = Fernet(self.kek)
        encrypted_secret = f.encrypt(encoded_secret)

        print(encrypted_secret)
        print(type(encrypted_secret))
        return encrypted_secret

    def store_kek_ciphertext(self, ciphertext):
        print("storing")
        KekRepository.create(1, ciphertext, "final")

    def fetch_kek_ciphertext_from_store(self):
        print("fetching")
        return KekRepository.get(cid=1)

    def decrypt_kek_ciphertext(self, ciphertext):
        print('decrypting ciphertext')
        text = self.kms_client.decrypt(KeyId='alias/foo', CiphertextBlob=ciphertext)['Plaintext']
        print(text)
        print(base64.b64encode(text))
        return text

    def setup(self):
        print("in setup")
        kek = self.fetch_kek_ciphertext_from_store()
        print(kek)
        if not kek:
            response = self.generate_kek()
            #print(response["CiphertextBlob"], base64.b64encode(response["Plaintext"]))
            #print("first decrypt")
            #print("cblob 1")
            #print(type(response["CiphertextBlob"]))
            #print(response["CiphertextBlob"])
            self.decrypt_kek_ciphertext(response["CiphertextBlob"])
            self.kek = base64.b64encode(response["Plaintext"])
            self.store_kek_ciphertext(response["CiphertextBlob"])
        else:
            print("kek ciphertext found in db")
            #print(kek)
            #print(type(kek))
            #print(type(kek.__dict__['ciphertext']))
            #print(kek.__dict__['ciphertext'])
            self.kek =  base64.b64encode(self.decrypt_kek_ciphertext(kek.__dict__['ciphertext']))
            #print(self.kek)

