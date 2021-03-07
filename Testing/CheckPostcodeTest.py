from postcode_validator_uk.validators import UKPostcode

def checkPostcode(postcode):
    try:
        UKPostcode(postcode).validate()  # If this statement fails then we know that the postcode provided is not valid.
        return True
    except:
        return False

#Valid Data
print(checkPostcode("CF314QR"))

#Valid data with spaces
print(checkPostcode("CF31 4QR"))

#Valid data lowercase
print(checkPostcode("cf31 4qr"))

#Correct Format wrong syntax (CANT EXIST)
print(checkPostcode("ZZ11 1ZZ"))

#Empty string
print(checkPostcode(""))

#long random string
print(checkPostcode("ahfjkgasjklfjkas"))

#random string correct length
print(checkPostcode("jdfijd8"))

#just numbers
print(checkPostcode("1234567"))