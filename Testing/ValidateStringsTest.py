def validatePlainString(strng, numCheck=False):
    strng = strng.replace(" ","")
    strng = strng.replace("-", "")  # Strings are allowed to have dashes
    if strng.isalnum() == False:  # IF THE STRING IS NOT ALPHANUMERIC RETURN FALSE
        return False

    if numCheck == True:
        c = 0  # counts the number of numbers encountered
        for i in strng:  # cycles through the characters in the string
            if i.isnumeric() == True:  # checks if the character is a number
                c += 1  # increments the count
        if c > 0:  # checks if there were any numbers in the string
            return False  # return false for not valid if yes

    return True

##Number Check Off Tests

#Normal Alpha Numeric String
print(validatePlainString("Hello 99"))

#Just Letters
print(validatePlainString("Hello World"))

#Just Numbers
print(validatePlainString("12345"))

#Empty String
print(validatePlainString(""))

#Contains punctuation other than -
print(validatePlainString("!£$%^&*)"))

#Complex String (such as address)
print(validatePlainString("9 Pen-Y-Hen"))

##Number Check On Tests
print("Num Check On")

#Normal Alpha Numeric String
print(validatePlainString("Hello 99",numCheck=True))

#Just Letters
print(validatePlainString("Hello World",numCheck=True))

#Just Numbers
print(validatePlainString("12345",numCheck=True))

#Empty String
print(validatePlainString("",numCheck=True))

#Contains punctuation other than -
print(validatePlainString("!£$%^&*)",numCheck=True))

