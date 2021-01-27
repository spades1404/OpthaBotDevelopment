import hashlib
import os
import base64

encoding = "utf-8"

class Passwords():
    def __init__(self):
        return
    def generatedSaltedHash(self,password):
        salt = os.urandom(32) #Generates a 32 bit key
        key = hashlib.pbkdf2_hmac(
            "sha256", # Hash algorithm it uses
            password.encode("utf-8"), # Converts the password to bytes
            salt, # Our salt
            100000, # Iterations of SHA-256
            dklen=64 # Get a 128 byte key
        )


        return salt+key

    def confirmPassDeprecated(self,password,hash):
        if password == hash:
            return True
        else:
            return False

    def confirmPass(self,password,hash):


        print(password)
        print(hash)

        salt = hash[:32].encode()
        key = hash[32:].encode()

        newKey = hashlib.pbkdf2_hmac(
            "sha256",  # Hash algorithm it uses
            password.encode(),  # Converts the password to bytes
            salt,  # Our salt
            100000,  # Iterations of SHA-256
            dklen=64  # Get a 128 byte key
        )
        print(newKey)
        print(type(newKey))

        if newKey == key:
            return True
        else:
            return False



if __name__ == "__main__":
    #UNIT TEST
    example_pass = "password"
    hashed = Passwords().generatedSaltedHash(example_pass)

    hashed = str(hashed)


    print(Passwords().confirmPass(example_pass,hashed))

    #print(Passwords().generatedSaltedHash("pass"))