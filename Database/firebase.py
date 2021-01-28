#Database Imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as fs
import pyrebase #This one lets use access firebase storage - others do not
import json #For reading our config files
from difflib import SequenceMatcher #For search queries


from Class.validation import Validation
from Class.directories import Directories
from Class.hashing import Passwords
class Database(): #Defining the firebase class inside the main window class because of PyQt class handling oddities
    def __init__(self, dirs = None ):
        self.dirs = Directories()
        self.config = self.js_r(self.dirs.configFile)  # Firebase access key
        self.key = credentials.Certificate(self.dirs.keyFile)  # Firebase private key
        firebase_admin.initialize_app(self.key)  # Configures our lib with our db access key

        self.pbs = pyrebase.initialize_app(self.config)  # Pyrebase connection for accessing our storage
        self.storage = self.pbs.storage()  # This is our object for the storage database

        self.fsdb = fs.client()  # Object for accessing the firebase - where descriptive data is





    #############FIREBASE STORAGE################
    def saveToFirebaseStorage(self, filePath, pathOnServer):  # saving a file to our store
        self.storage.child(pathOnServer).put(filePath)  # Saves our file on the server

    def downloadFromFirebaseStorage(self, pathOnServer, outputName):  # Downloading a file from the store
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

    def createUser(self, fname, lname, username, email, password):
        return

    def returnUserFromID(self, ID):
        query = self.fsdb.collection(u"users")
        for doc in query.stream():
            if doc.id == ID:
                return doc.to_dict()

    def signIn(self, username, password):
        query = self.fsdb.collection(u"users")
        db = query.stream()
        for i in db:
            data = i.to_dict()

            if data["username"] == username:
                if Passwords().confirmPassDeprecated(password,data["password"]) == True:
                    return i

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
            "condition":scan.result,
            "custID":scan.custID,
            "location":serverLoc,
            "time":scan.scanTime
        }

        self.fsdb.collection(u"images").add(scanRes)

        return

    def similar(self,a,b):
        return SequenceMatcher(None,a,b).ratio()

    def searchPX(self,fName = "", lName = "", email = "", id="", postcode= "", phone="",addy=""):
        #THIS METHOD IS VERY SLOW FOR LARGE RECORDS
        collection = self.fsdb.collection(u"patients").stream() #This has all of our patient records
        scoreList = [] #This will store a list of simmilarity scores for each record
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

            total = s1+s2+s3+s4+s5+s6+s7

            allRecords.append(x)

            scoreList.append(total)

        allRecords = [x for _,x in sorted(zip(scoreList,allRecords))]

        #lets strip both lists
        for i in allRecords:
            index = allRecords.index(i)
            if scoreList[index] == 0:
                scoreList.pop(index)
                allRecords.pop(index)


        #allRecords = collection[:10]

        return allRecords[:10]






if __name__ == "__main__":
    db = Database()

