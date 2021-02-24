#Database Imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as fs
import pyrebase  # This one lets use access firebase storage - others do not
import json  # For reading our config files
from difflib import SequenceMatcher  # For search queries
import datetime
import string
import random

# we are importing these classes seperately and not through the global funcs because globalfuncs depends on having access to the database class which causes a ciruclar import
from Class.validation import Validation
from Class.directories import Directories
from Class.hashing import Passwords
from Class.user import Patient

import pytz
import os


class Database():  # Defining the firebase class inside the main window class because of PyQt class handling oddities
    def __init__(self, dirs=None):
        self.dirs = Directories()
        self.config = self.js_r(self.dirs.configFile)  # Firebase access key
        self.key = credentials.Certificate(self.dirs.keyFile)  # Firebase private key
        firebase_admin.initialize_app(self.key)  # Configures our lib with our db access key

        self.pbs = pyrebase.initialize_app(self.config)  # Pyrebase connection for accessing our storage
        self.storage = self.pbs.storage()  # This is our object for the storage database

        self.fsdb = fs.client()  # Object for accessing the firebase - where descriptive data is

        self.initPracticeCode()

    def initPracticeCode(self):
        self.practice = self.js_r(self.dirs.appPermaSets)["practice"]

    #############FIREBASE STORAGE################
    def saveToFirebaseStorage(self, filePath, pathOnServer):  # saving a file to our store
        self.storage.child(pathOnServer).put(filePath)  # Saves our file on the server

    def downloadFromFirebaseStorage(self, pathOnServer, outputName):  # Downloading a file from the store
        if os.path.exists(outputName) == False:
            self.storage.child(pathOnServer).download(outputName)  # Grabs our file from the server and downloads

    ##################################################


    ##ORGS##
    def addOrganisation(self,name,mainAdmin,contactNum,contactEmail,postcode,address,city):
        name = str(name)
        mainAdmin = str(mainAdmin)
        contactNum = str(contactNum)
        contactEmail = str(contactEmail)
        postcode = str(postcode)
        address = str(address)
        city = str(city)

        #Verify Contents
        if Validation().validatePlainString(name,numCheck=True) or Validation().validatePlainString(mainAdmin,numCheck=True)  or Validation().checkEmail(contactEmail) or Validation().checkNumber(contactNum) or Validation().checkPostcode(postcode) or Validation().validatePlainString(address) or Validation().validatePlainString(city,numCheck=True) == False:
            return "Invalid Details Cannot Make Org"


        org = {
            "name": name,
            "mainAdmin" : mainAdmin,
            "contactNum" : contactNum,
            "contactEmail" : contactEmail,
            "postcode" : postcode,
            "address" : address,
            "city" : city
        }

        self.fsdb.collection(u"organisations").add(org)

        return True

    def returnAllOrgs(self):
        return [i for i in self.fsdb.collection(u"organisations").stream()]


    #def editOrganisation(self,dic):
    #    if Validation().validatePlainString(dic["name"],numCheck=True) or Validation().validatePlainString(dic["mainAdmin"],numCheck=True)  or Validation().checkEmail(dic["contactEmail"]) or Validation().checkNumber(dic["contactNum"]) or Validation().checkPostcode(dic["postcode"]) or Validation().validatePlainString(["address"]) or Validation().validatePlainString(dic["city"],numCheck=True) == False:
    #        return "Invalid Details Cannot Make Org"

    def returnCollectionContents(self, collectionDir):
        query = self.fsdb.collection(collectionDir)
        for doc in query.stream():
            print(doc)
            print("{} => {}".format(doc.id, doc.to_dict()))

    def makeUserAdmin(self, tag):
        return

    def createUser(self, fname, lname, email, user, passw, access, id):
        return self.fsdb.collection(u"users").add({
            "accessLevel": access,
            "email": email,
            "fName": fname,
            "lName": lname,
            "username": user,
            "password": passw,
            "practice": id
        })[1]

    def returnUserFromID(self, ID):
        query = self.fsdb.collection(u"users")
        for doc in query.stream():
            if doc.id == ID:
                return doc.to_dict()

    def signIn(self, username, password):
        db = self.fsdb.collection(u"users").where("practice", "==", self.practice).where("username", "==",
                                                                                         username).get()

        print(db)
        if Passwords().confirmPassDeprecated(password, db[0].to_dict()["password"]) == True:
            return db[0]

        return None




    def checkForUpdate(self):#this function will check for model updates from the server
        query = self.fsdb.collection(u"models")
        data = [i.to_dict() for i in query.stream()]  # Grabs data and converst all jsons into dictionaries
        x = sorted(data, key=lambda key: key["date"], reverse=True)  # sorts the data by date from latest to earliest
        newestModel = x[0]

        with open(self.dirs.currMod, "r") as file:
            if newestModel.id == file.read():
                return newestModel
            else:
                return False



    def generatePlaceholderFile(self,name):
        with open(name,"w") as file:
            file.close()

    def js_r(self,filename):
        with open(filename) as f_in:
            return (json.load(f_in))

    def uploadScan(self,scan):

        serverLoc = "Images/" + scan.fileName
        self.saveToFirebaseStorage(scan.postProcessDir,serverLoc)
        scanRes = {
            "condition": scan.result,
            "custID": scan.custID,
            "location": serverLoc,
            "time": scan.scanTime,
            "diagnosis": "",
            "practice": self.practice
        }

        result = self.fsdb.collection(u"images").add(scanRes)
        scan.serverID = result[1].id
        scan.uploaded = True
        print(scanRes)

        return

    def addNewPX(self, fname, lname, email, id, postcode, phone, addy, date):
        dict = {
            "fName": fname,
            "lName": lname,
            "email": email,
            "orgID": id,
            "postcode": postcode,
            "phoneNumber": phone,
            "addressLine": addy,
            "dob": date,
            "practice": self.practice
        }

        return self.fsdb.collection(u"patients").add(dict)[0].id

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def generateNewIDFromDB(self, field, collection):
        try:
            ids = [i.to_dict()[field] for i in self.fsdb.collection(collection).stream()]
            x = ids[0]  # if the collection is empty its safe to return any new string
        except:
            x = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
            return x

        while x in ids:
            x = ''.join(random.choice(string.ascii_uppercase) for i in range(6))

        return x

    def compareDate(self, date1, date2):

        if date1.strftime("%d:%m:%Y") == date2.strftime("%d:%m:%Y"):
            return True
        else:
            return False

    def searchPX(self,fName = "", lName = "", email = "", id="", postcode= "", phone="",addy="",date=None):
        #THIS METHOD IS VERY SLOW FOR LARGE RECORDS
        collection = self.fsdb.collection(u"patients").where("practice", "==",
                                                             self.practice).get()  # This has all of our patient records
        scoreList = []  #This will store a list of simmilarity scores for each record
        allRecords = []

        for i in collection:
            x = i.to_dict()
            s1 = (self.similar(fName,x["fName"]))/7
            s2 = (self.similar(lName, x["lName"]))/7
            s3 = (self.similar(email, x["email"]))/7
            s4 = (self.similar(id, x["orgID"]))/3 #we give this a higher weighting
            s5 = (self.similar(postcode, x["postcode"]))/7
            s6 = (self.similar(phone, x["phoneNumber"]))/7
            s7 = (self.similar(addy, x["addressLine"]))/7


            try:
                y = x["dob"]
                if y == date:
                    s8 = 1
                else:
                    s8 = 0
            except Exception as e:
                s8=0


            total = s1+s2+s3+s4+s5+s6+s7+s8


            allRecords.append(i)

            scoreList.append(total)

        #
        multidlist = []
        for i in range(len(allRecords)):
            multidlist.append([allRecords[i],scoreList[i]])

        multidlist = sorted(multidlist, key=lambda x: x[1], reverse=True)

        allRecords = [Patient(i[0]) for i in multidlist if i[1] > 0.05]


        return allRecords[:10]

    def updateScanPXLink(self,sourceID,linkID):
        record = self.fsdb.collection(u"images").document(sourceID)
        record.update({"custID":linkID})

    def updateDiagnosis(self,sourceID,cond):
        record = self.fsdb.collection(u"images").document(sourceID)
        record.update({"diagnosis": cond})

    def returnRecentScans(self, filter):  # filter =1 for past day =2 for past week =3 for past month
        try:
            result = self.fsdb.collection(u"images").where("practice", "==", self.practice).get()
        except Exception as e:
            print(e)
            print("no scans :(")
            return []
        start = datetime.datetime.now()

        d = 1
        if filter == 1:
            d = 1
        elif filter == 2:
            d = 7
        elif filter == 3:
            d = 30
        end = datetime.datetime.now() - datetime.timedelta(days=d)

        filtered = [i for i in result if pytz.UTC.localize(end) <= i.to_dict()["time"] <= pytz.UTC.localize(start)]

        return filtered

    def returnScansFromUser(self, id):
        return self.fsdb.collection(u"images").where("custID", "==", id).get()

    def returnPracticeByLink(self, code):
        return self.fsdb.collection(u"practices").where("linkCode", "==", code).get()

    def returnOrgByLink(self, code):
        return self.fsdb.collection(u"organisations").where("linkCode", "==", code).get()

    def addNewPractice(self, name, admin, email, phone, addr, post, org):
        data = {
            "name": name,
            "adminName": admin,
            "contactEmail": email,
            "contactNum": phone,
            "address": addr,
            "postcode": post,
            "organisation": org,
            "linkCode": self.generateNewIDFromDB("linkCode", u"practices")
        }
        x = self.fsdb.collection(u"practices").add(data)[1]
        return x


if __name__ == "__main__":
    db = Database()

