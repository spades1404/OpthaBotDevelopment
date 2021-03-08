import os

import bcrypt
from cryptography.fernet import Fernet
from password_validator import PasswordValidator


class Password():
    def __init__(self):
        self.schema = PasswordValidator() #initiate password validator class
        self.schema.min(8).max(100).has().digits().has().uppercase().has().lowercase().has().no().spaces() #setting up the schema for our needs (8 or more chars, lowercase,uppercase,numbers)
        return

    def genHash(self, passw):
        return bcrypt.hashpw(passw.encode(), bcrypt.gensalt()) #generates a salted bcrypt hash from a plaintext password

    def checkHash(self, passw, hash):
        print(bcrypt.checkpw(passw.encode(), hash))
        return bcrypt.checkpw(passw.encode(), hash) #checks a plain text password against a given hash

    def checkPasswordIsValid(self, passw):
        return self.schema.validate(passw) #checks if a plain text password fits within the schema we made


class AES():
    def __init__(self):
        return

    def genKey(self,depositDir): #Takes the directory you want to save the key to as parameter
        key = Fernet.generate_key() #Generate a key
        with open(depositDir+r"\key.key","wb") as keyFile: #open the file
            keyFile.write(key) #write the key to the file

    def loadKey(self,filename):
        key = open(filename,"rb").read() #opens and reads the file as bytes
        self.key = key #sets class attribute as key
        return self

    def encrypt(self,inputFilename,outputFilename):
        f = Fernet(self.key) #initialize Fernet with key
        with open(inputFilename, "rb") as file: #open the file that needs to be encrypted
            # read all file data
            file_data = file.read() #save the read text

        encrypted = f.encrypt(file_data) #encrypt the file contents

        # write the encrypted file
        with open(outputFilename, "wb") as file: #open the output file
            file.write(encrypted) #write the encrypted data to the output file


    def decrypt(self,inputFilename,outputFilename):
        f = Fernet(self.key)#initialize Fernet with key
        with open(inputFilename, "rb") as file:#open the file that needs to be decrypted
            # read all file data
            file_data = file.read()#save the read text

        decrypted = f.decrypt(file_data).decode("utf-8","ignore").replace("\n","")#decrypt the file contents, decode the file and remove newlines that are generated from the decoding



        # write the encrypted file
        with open(outputFilename, "w",encoding="utf-8") as file: #open the output file
            file.write(decrypted) #write the data to the output file

        return outputFilename


if __name__ == "__main__":
    os.chdir(r"C:\Users\rajib\Documents\GitHub\OpthaBotDevelopment")
    e = AES()

    #e.genKey("Assets")
    e.loadKey(r"Assets\key.key")

    e.encrypt(r"C:\Users\rajib\AppData\Local\Temp\tmpraff7dfo\config.txt",r"Assets\config.txt")
    #e.decrypt(r"Assets\Encryptiontest\output.txt",r"Assets\Encryptiontest\noway.txt")