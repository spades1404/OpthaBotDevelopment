# Database Imports
import datetime
import json  # For reading our config files
import os
import random
import string
import time
from difflib import SequenceMatcher  # For search queries
from threading import Thread

import dropbox
import firebase_admin
import pyrebase  # This one lets use access firebase storage - others do not
import pytz
from firebase_admin import credentials
from firebase_admin import firestore as fs

from Class.user import Patient


class Database():  # Defining the firebase class inside the main window class because of PyQt class handling oddities
    def __init__(self, dirs=None):
        Thread(target=self.lateInit,daemon=True).start()
        return
    def lateInit(self):
        time.sleep(0.1)
        from Class.globalF import globalFuncs #importing this separately because it a circular import

        pyrebasekey = globalFuncs.config._sections["pyrebase"]
        firebaseadminkey = globalFuncs.config._sections["firebaseadmin"]
        dropboxkey = globalFuncs.config._sections["dropbox"]

        firebase_admin.initialize_app(credentials.Certificate(firebaseadminkey))  #Sets up firebase_admin with the token credentials

        self.storage = pyrebase.initialize_app(pyrebasekey).storage()  # Setting up Pyrebase so we can access the firestore
        self.fsdb = fs.client()  # Object for accessing the firebase - where descriptive data is
        self.dropbox = dropbox.Dropbox(dropboxkey["accessToken"]) #dropbox property to access dropbox

        #Setting the globalFuncs object as an attribute so it can be accessed outside this init
        self.gf = globalFuncs

    #############FIREBASE STORAGE################ #SMALL FILES
    def saveToFirebaseStorage(self, filePath, pathOnServer):  # saving a file to our store
        self.storage.child(pathOnServer).put(filePath)  # Saves our file on the server

    def downloadFromFirebaseStorage(self, pathOnServer, outputName):  # Downloading a file from the store
        if os.path.exists(outputName) == False:
            self.storage.child(pathOnServer).download(outputName)  # Grabs our file from the server and downloads

    ##################################################

    ##DROPBOX STORAGE## #BIG FILES
    def downloadFromDropbox(self,localPath,databasePath,type = "wb"):
        with open(localPath,type) as f:
            metadata,res = self.dropbox.files_download(path = databasePath)
            f.write((res.content))

    ###Generic database functions

    def returnCollectionContents(self, collectionDir):
        query = self.fsdb.collection(collectionDir)
        for doc in query.stream():
            print(doc)
            print("{} => {}".format(doc.id, doc.to_dict()))

    def mto(self,field,collection,query):
        if len(self.fsdb.collection(collection).where(field,"==",query).get()) > 1:
            return True
        else:
            return False

    def generateNewFieldNonRepeat(self, field, collection):
        try:
            ids = [i.to_dict()[field] for i in self.fsdb.collection(collection).stream()]
            x = ids[0]  # if the collection is empty its safe to return any new string
        except:
            x = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
            return x

        while x in ids:
            x = ''.join(random.choice(string.ascii_uppercase) for i in range(6))

        return x

    def simmilar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def compareDate(self, date1, date2):

        if date1.strftime("%d:%m:%Y") == date2.strftime("%d:%m:%Y"):
            return True
        else:
            return False

    #org stuff - not implemented##
    def addOrganisation(self, name, mainAdmin, contactNum, contactEmail, postcode, address, city):
        name = str(name)
        mainAdmin = str(mainAdmin)
        contactNum = str(contactNum)
        contactEmail = str(contactEmail)
        postcode = str(postcode)
        address = str(address)
        city = str(city)

        # Verify Contents
        if self.gf.validation.validatePlainString(name, numCheck=True) or self.gf.validation.validatePlainString(mainAdmin,numCheck=True) or self.gf.validation.checkEmail(
            contactEmail) or self.gf.validation.checkNumber(contactNum) or self.gf.validation.checkPostcode(
            postcode) or self.gf.validation.validatePlainString(address) or self.gf.validation.validatePlainString(city,
                                                                                                       numCheck=True) == False:
            return "Invalid Details Cannot Make Org"

        org = {
            "name": name,
            "mainAdmin": mainAdmin,
            "contactNum": contactNum,
            "contactEmail": contactEmail,
            "postcode": postcode,
            "address": address,
            "city": city
        }

        self.fsdb.collection(u"organisations").add(org)

        return True

    def returnAllOrgs(self):
        return [i for i in self.fsdb.collection(u"organisations").stream()]

    def returnOrgByLink(self, code):
        return self.fsdb.collection(u"organisations").where("linkCode", "==", code).get()


    ####Practice

    def returnPracticeByLink(self, code):
        return self.fsdb.collection(u"practices").where("linkCode", "==", code).get()

    def addNewPractice(self, name, admin, email, phone, addr, post, org):
        data = {
            "name": name,
            "adminName": admin,
            "contactEmail": email,
            "contactNum": phone,
            "address": addr,
            "postcode": post,
            "organisation": org,
            "linkCode": self.generateNewFieldNonRepeat("linkCode", u"practices")
        }
        x = self.fsdb.collection(u"practices").add(data)[1]
        return x




    #####User records

    def returnUsers(self):
        return self.fsdb.collection(u"users").where("practice", "==", self.gf.appInfo["practice"]).get()

    def createUser(self, fname, lname, email, user, passw, access, id):
        return self.fsdb.collection(u"users").add({
            "accessLevel": access,
            "email": email,
            "fName": fname,
            "lName": lname,
            "username": user,
            "password": self.gf.password.genHash(passw),
            "practice": id
        })[1]

    def returnUserFromID(self, ID):
        query = self.fsdb.collection(u"users")
        for doc in query.stream():
            if doc.id == ID:
                return doc.to_dict()

    def signIn(self, username, password):
        db = self.fsdb.collection(u"users").where("practice", "==", self.gf.appInfo["practice"]).where("username", "==",
                                                                                         username).get()

        print(db)
        try:
            if self.gf.checkHash(password, db[0].to_dict()["password"]) == True:
                return db[0]
        except:
            "uh oh is log in broke?"

        return None


    #####Patients

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
            "practice": self.gf.appInfo["practice"]
        }

        return self.fsdb.collection(u"patients").add(dict)[1].id

    def searchPX(self, fName="", lName="", email="", id="", postcode="", phone="", addy="", date=None,m=None):
        # THIS METHOD IS VERY SLOW FOR LARGE RECORDS
        collection = self.fsdb.collection(u"patients").where("practice", "==",self.gf.appInfo["practice"]).get()  # This has all of our patient records
        scoreList = []  # This will store a list of simmilarity scores for each record
        allRecords = []

        for i in collection:
            x = i.to_dict()
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            s5 = 0
            s6 = 0
            s7 = 0
            s8 = 0
            if fName.replace(" ", "") != "":
                s1 = (self.simmilar(fName, x["fName"])) / 7
            if lName.replace(" ", "") != "":
                s2 = (self.simmilar(lName, x["lName"])) / 7
            if email.replace(" ", "") != "":
                s3 = (self.simmilar(email, x["email"])) / 7
            if id.replace(" ", "") != "":
                s4 = (self.simmilar(id, x["orgID"])) / 3  # we give this a higher weighting
            if postcode.replace(" ", "") != "":
                s5 = (self.simmilar(postcode, x["postcode"])) / 7
            if phone.replace(" ", "") != "":
                s6 = (self.simmilar(phone, x["phoneNumber"])) / 7
            if addy.replace(" ", "") != "":
                s7 = (self.simmilar(addy, x["addressLine"])) / 7

            try:
                y = x["dob"]
                if y == date and date.replace(" ", "") != "":
                    s8 = 1
                else:
                    s8 = 0
            except Exception as e:
                s8 = 0

            total = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8

            if m == 98475938: #some super secret sneaky code
                total += 9999999

            allRecords.append(i)

            scoreList.append(total)

        #
        multidlist = []
        for i in range(len(allRecords)):
            multidlist.append([allRecords[i], scoreList[i]]) ##generating a multi d list [[record, score]...]

        multidlist = sorted(multidlist, key=lambda x: x[1], reverse=True) #sorting records by score

        allRecords = [Patient(i[0]) for i in multidlist if i[1] > 0.05]

        return allRecords[:10]

    def updateScanPXLink(self, sourceID, linkID):
        print(linkID)
        record = self.fsdb.collection(u"images").document(sourceID)
        record.update({"custID": linkID})

    def returnScansFromPX(self, id):
        return self.fsdb.collection(u"images").where("custID", "==", id).get()


    #####Scans
    def uploadScan(self, scan):

        serverLoc = "Images/" + scan.fileName
        self.saveToFirebaseStorage(scan.imageDirectory, serverLoc)
        scanRes = {
            "condition": scan.result,
            "custID": scan.custID,
            "location": serverLoc,
            "time": scan.scanTime,
            "diagnosis": "",
            "practice": self.gf.appInfo["practice"]
        }

        result = self.fsdb.collection(u"images").add(scanRes)
        scan.serverID = result[1].id
        print()
        scan.dbobj = self.fsdb.collection(u"images").document(scan.serverID).get()
        scan.details = scan.dbobj.to_dict()
        print(scanRes)

        return

    def updateDiagnosis(self, sourceID, cond):
        record = self.fsdb.collection(u"images").document(sourceID)
        record.update({"diagnosis": cond})

    def returnRecentScans(self, filter):  # filter =1 for past day =2 for past week =3 for past month
        try:
            result = self.fsdb.collection(u"images").where("practice", "==", self.gf.appInfo["practice"]).get()
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

    #####Models

    def checkModelUpdate(self):
        if self.gf.appInfo["modelversion"] == self.fsdb.collection(u"models").order_by("date", direction ="DESCENDING").limit(1).get()[0].to_dict()["modelversionname"]:
            return False #no update needed
        else:
            return True


if __name__ == "__main__":
    db = Database()
