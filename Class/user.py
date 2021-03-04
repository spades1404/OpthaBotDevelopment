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

    def changePW(self):
        return


    def updatePXdetails(self,fname,lname,email,id,postcode,phone,addy,date):
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
