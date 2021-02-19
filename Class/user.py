from Database.firebase import Database

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
        self.accessLevel = self.details["accessLevel"]
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
        self.scans = self.details["scans"]
        return