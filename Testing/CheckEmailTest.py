from validate_email import validate_email

def checkEmail(email):
    return validate_email(email)  # Validating using this lib function


#Valid email
print(checkEmail("rajibahmed@gmail.com"))

#Nothing
print(checkEmail(""))

#random string
print(checkEmail("jksagfdduioasw4aahsduoifh"))

#random string with an @ and . in it
print(checkEmail("jklsadgfouias@asdfuiasihdf.ciohaosh"))

