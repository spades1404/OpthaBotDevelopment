import os

import bcrypt
from cryptography.fernet import Fernet
from password_validator import PasswordValidator


class Password():
    def __init__(self):
        self.schema = PasswordValidator()
        self.schema.min(8).max(100).has().digits().has().uppercase().has().lowercase().has().no().spaces()
        return

    def genHash(self, passw):
        return bcrypt.hashpw(passw.encode(), bcrypt.gensalt())

    def checkHash(self, passw, hash):
        return bcrypt.checkpw(passw.encode(), hash)

    def checkPasswordIsValid(self, passw):
        return self.schema.validate(passw)


class AES():
    def __init__(self):
        return

    def genKey(self,depositDir):
        key = Fernet.generate_key()
        with open(depositDir+r"\key.key","wb") as keyFile:
            keyFile.write(key

    )

    def loadKey(self,filename):
        key = open(filename,"rb").read()
        self.key = key
        return self

    def encrypt(self,inputFilename,outputFilename):
        f = Fernet(self.key)
        with open(inputFilename, "rb") as file:
            # read all file data
            file_data = file.read()

        encrypted = f.encrypt(file_data)

        # write the encrypted file
        with open(outputFilename, "wb") as file:
            file.write(encrypted)


    def decrypt(self,inputFilename,outputFilename):
        f = Fernet(self.key)
        with open(inputFilename, "rb") as file:
            # read all file data
            file_data = file.read()

        decrypted = f.decrypt(file_data).decode("utf-8","ignore").replace("\n","")



        # write the encrypted file
        with open(outputFilename, "w",encoding="utf-8") as file:
            file.write(decrypted)

        #print(decrypted.decode("utf-8","ignore"))
        return outputFilename


if __name__ == "__main__":
    os.chdir(r"C:\Users\rajib\OneDrive\Documents\Github\OpthaBotDevelopment")
    e = AES()

    e.genKey("Assets")
    e.loadKey("Assets\key.key")

    e.encrypt(r"Assets\Encryptiontest\test.txt",r"Assets\config.txt")
    #e.decrypt(r"Assets\Encryptiontest\output.txt",r"Assets\Encryptiontest\noway.txt")