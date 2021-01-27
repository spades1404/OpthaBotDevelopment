import requests
from validate_email import validate_email
from postcode_validator_uk.validators import UKPostcode
import string
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from PIL import Image


class Validation():
    def __init__(self):
        return

    def checkWifi(self):
        try:
            r = requests.get("http://www.google.com",timeout = 20)
            return True
        except:
            return False

    def checkEmail(self,email):
        return validate_email(email) #Validating using this lib function

    def checkPostcode(self,postcode):
        try:
            UKPostcode(postcode).validate()
            return True
        except:
            return False

    def validatePlainString(self,strng,numCheck=False):
        for i in strng:
            if i in string.punctuation.replace("-",""):
                return False
        if numCheck == True:
            for i in strng:
                if i.isnumeric() == True:
                    return False

        return True

    def checkNumber(self,num): #verifies phone numbers NUMBER MUST BE STR
        try:
            return carrier._is_mobile(number_type(phonenumbers.parse(num,"GB")))
        except:
            return False

    def checkImage(self,source):
        try:
            Image.open(source)
            return True
        except:
            return False




if __name__ == "__main__":

    #UNIT TEST (Redacted personal info after test)
    x = Validation()

    #CHECK WIFI FUNC
    print(x.checkWifi())

    #VAL EMAIL FUNC
    print(x.checkEmail("INFO HERE"))

    #POSTCODE FUNC
    print(x.checkPostcode("INFO HERE"))

    #STRING FUNC
    print(x.validatePlainString("Rajib"))
    print(x.validatePlainString("Raji*(&^%b"))
    print(x.validatePlainString("Rajib1",numCheck=True))
    print(x.validatePlainString("Rajib", numCheck=True))

    #NUM FUNC
    print(x.checkNumber("INFO HERE"))


