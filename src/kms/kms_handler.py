import boto3
import json
import base64


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

        if not self.kek:
            response = self.kms_client.generate_data_key(KeyId='alias/foo', KeySpec='AES_256')
            print(response["CiphertextBlob"], base64.b64encode(response["Plaintext"]))
            self.kek = response["Plaintext"]

    def decrypt_secret(self):
        pass

    def encrypt_secret(self):
        pass

    def store_kek_ciphertext(self):
        pass

    def fetch_kek_ciphertext_from_store(self):
        pass

    def decrypt_kek_ciphertext(self):
        pass

    def setup(self):
        #search in DB
        #if found, load and decrypt
        #else
        #generate
