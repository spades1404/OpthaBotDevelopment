import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

def checkNumber(num): #verifies phone numbers NUMBER MUST BE STR

    try:
        parsed = phonenumbers.parse(num, "GB")
        if number_type(parsed) == 0 or number_type(parsed) == 1 or number_type(parsed) == 99:
            return True
        else:
            return False
    except:
        return False

#Local UK number
print(checkNumber("01656658191"))

#UK Mobile numberUK Hom
print(checkNumber("07163296058"))

#UK Mobile number with area code
print(checkNumber("+441632960586"))

#UK Number with appropriate spacing
print(checkNumber("01632 960586"))

#UK Number with random spacing
print(checkNumber("07 163 29605 86"))

#Random Number
print(checkNumber("03485034223"))

#Empty String
print(checkNumber(""))

#Random String
print(checkNumber("OneTwoThree"))


