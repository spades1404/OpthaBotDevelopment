from Class.validation import Validation
class Profile(): #Base profile super class
    def __init__(self,obj):
        self.document = obj
        self.details = obj.to_dict()

        self.id = self.document.id
        self.fname = self.details["fName"]
        self.lname = self.details["lName"]
        self.email = self.details["email"]



        return


class User(Profile):
    def __init__(self,obj):
        super(User, self).__init__(obj)
        self.accessLevel = int(self.details["accessLevel"])
        self.username = self.details["username"]
        return


class Patient(Profile):
    def __init__(self,obj):
        super(Patient, self).__init__(obj)
        self.addressLine = self.details["addressLine"]
        self.dob = self.details["dob"]
        self.orgID = self.details["orgID"]
        self.phoneNum = self.details["phoneNumber"]
        self.postcode = self.details["postcode"]
        return


    def updatePXdetails(self,fname,lname,email,id,postcode,phone,addy,date):
        '''
        f = [fname, lname, email, id, postcode, phone, addy]
        for i in [i.replace(" ", "") for i in f]:
            if i == "":
                return "Not all fields filled"

        validation = Validation()

        if validation.validatePlainString(fname,numCheck=True) == False or validation.validatePlainString(lname, numCheck=True) == False:
            return "Name must not have numbers"

        if validation.checkEmail(email) == False:
            return "Invalid Email"

        if validation.validatePlainString(id) == False:
            return "ID is not a valid string"

        if validation.checkNumber(phone) == False:
            return "Invalid Number"

        if validation.checkDate(date) == False:
            return "Invalid Date"

        # if globalFuncs.validation.validatePlainString(addy) == False:
        #    return "Address is not a valid string"

        if validation.checkPostcode(postcode) == False:
            return "Postcode is not valid"

        '''

        changes = {}
        if fname.replace(" ","") != "" and self.details["fName"] != fname:
            changes["fName"] = fname
        elif lname.replace(" ","") != "" and self.details["lName"] != lname:
            changes["lName"] = lname
        elif email.replace(" ","") != "" and self.details["email"] != email:
            changes["email"] = email
        elif id.replace(" ","") != "" and self.details["orgID"] != id:
            changes["orgID"] = id
        elif postcode.replace(" ","") != "" and self.details["postcode"] != postcode:
            changes["postcode"] = postcode
        elif phone.replace(" ","") != "" and self.details["phoneNumber"] != phone:
            changes["phoneNumber"] = phone
        elif addy.replace(" ","") != "" and self.details["addressLine"] != addy:
            changes["addressLine"] = addy
        elif date.replace(" ","") != "" and self.details["dob"] != date:
            changes["dob"] = date

        if changes != {}:
            print(self.document.reference.update(changes))

        return True
