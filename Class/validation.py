import requests
from validate_email import validate_email
from postcode_validator_uk.validators import UKPostcode
import string
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from PIL import Image
import datetime


class Validation():
    def __init__(self):
        return

    def checkWifi(self):
        try:
            r = requests.get("http://www.google.com",timeout = 20) # Send request to google, it will timeout with exception if it fails
            return True # We are connected to wifi
        except:
            return False # We are not connected to wifi

    def checkEmail(self,email):
        return validate_email(email) #Validating using this lib function

    def checkPostcode(self,postcode):
        try:
            UKPostcode(postcode).validate() #If this statement fails then we know that the postcode provided is not valid.
            return True
        except:
            return False

    def validatePlainString(self,strng,numCheck=False):
        strng.replace("-","") #Strings are allowed to have dashes
        if strng.isalnum() == False:  # IF THE STRING IS NOT ALPHANUMERIC RETURN FALSE
            return False

        if numCheck == True:
            c = 0 #counts the number of numbers encountered
            for i in strng: #cycles through the characters in the string
                if i.isnumeric() == True: #checks if the character is a number
                    c += 1 #increments the count
            if c > 0: #checks if there were any numbers in the string
                return False #return false for not valid if yes

        return True

    def checkNumber(self,num,*args):  # verifies phone numbers NUMBER MUST BE STR
        print(locals())
        try:
            parsed = phonenumbers.parse(num, "GB")
            if number_type(parsed) == 0 or number_type(parsed) == 1 or number_type(parsed) == 99:
                return True
            else:
                return False
        except:
            return False

    def checkImage(self,source):
        try:
            Image.open(source) #Try and open the image
            return True
        except:
            return False

    def checkDate(self, date):
        try:
            date = datetime.datetime.strptime(date, '%d/%m/%Y')
            return True

        except Exception as e:
            return False


if __name__ == "__main__":

    #UNIT TEST (Redacted personal info after test)
    x = Validation()

    #CHECK WIFI FUNC
    #print(x.checkWifi())

    #VAL EMAIL FUNC
    #print(x.checkEmail("INFO HERE"))

    #POSTCODE FUNC
    #print(x.checkPostcode("INFO HERE"))

    #STRING FUNC
    print(x.validatePlainString("Rajib"))
    print(x.validatePlainString("Raji*(&^%b"))
    print(x.validatePlainString("Rajib1",numCheck=True))
    print(x.validatePlainString("Rajib", numCheck=True))

    #NUM FUNC
    print(x.checkNumber("07951308773"))





