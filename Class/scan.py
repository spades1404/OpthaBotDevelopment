from datetime import datetime
from PIL import Image
from ImageProcessing.ImageFormatter import cropImageByColorDetection, resizeImage
from Class.globalF import globalFuncs
import random
import string
import numpy as np
class Scan():
    def __init__(self):
        return
    def initialiseFromProg(self,fileLoc):
        self.location = fileLoc
        self.scanTime = datetime.now()
        self.originalImage = Image.open(fileLoc)
        self.postProcessImage = self.preProcessImage(self.location)
        self.fileName = r"{}{}.jpg".format(globalFuncs.directories.temp,
                                           ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)))
        self.postProcessImage.save(self.fileName)
        self.custID = ""
        self.serverID = None
        self.uploaded = False

        return self

    def initialiseFromDB(self,obj):
        self.dbobj = obj
        self.details = self.dbobj.to_dict()
        self.serverID = self.dbobj.id
        self.custID = self.details["custID"]
        self.scanTime = self.details["time"]
        self.resultList = [
            ["Normal",self.details["condition"][0]],
            ["Diabetic Retinopathy",self.details["condition"][1]],
            ["Glaucoma",self.details["condition"][2]],
            ["Cataracts",self.details["condition"][3]],
            ["Age Related Macular Degeneration",self.details["condition"][4]],
            ["Hypertension",self.details["condition"][5]],
            ["Myopia",self.details["condition"][6]],
            ["Other Abnormalities",self.details["condition"][7]],
        ]

        return self

    def grabImage(self):
        self.imageDir = globalFuncs.directories.temp + (self.details["location"].split("/")[1])
        globalFuncs.database.downloadFromFirebaseStorage(self.details["location"], self.imageDir)
        self.postProcessDir = self.imageDir
        print(self.imageDir)

    def updateDetails(self, custid, condition, *args):  # will only update the customer id or the real condition
        if custid.replace(" ", "") != "":
            globalFuncs.database.updateScanPXLink(self.serverID, custid)
            self.custID = custid

        if condition.replace(" ", "") != "":
            globalFuncs.database.updateDiagnosis(self.serverID, condition)

    def preProcessImage(self, loc):
        image = cropImageByColorDetection(loc)  # Crops the image to the required content
        image = resizeImage(image, dim=256)
        return image

    def analyze(self): #this func takes a while
        #self.result = Tensorflow().analyzeImageSuccinct(self.postProcessImage)
        self.result = self.indiscriminateFunctionToGenerateRandomFloatNumbersInAListSizeXthatEnumerateToAnIntegerSizeN()
        print(self.result)
        self.generateMultiDiListofResults()#

    def generateTemp(self):
        self.postProcessDir = self.fileName
        self.postProcessImage.save(fp=self.postProcessDir)
        return self.postProcessDir

    def generateMultiDiListofResults(self):
        self.resultList = [
            ["Normal",self.result[0]],
            ["Diabetic Retinopathy",self.result[1]],
            ["Glaucoma",self.result[2]],
            ["Cataracts",self.result[3]],
            ["Age Related Macular Degeneration",self.result[4]],
            ["Hypertension",self.result[5]],
            ["Myopia",self.result[6]],
            ["Other Abnormalities",self.result[7]],
        ]

        self.resultList = sorted(self.resultList, key=lambda x: -x[1]) #Sort List by probability


    def indiscriminateFunctionToGenerateRandomFloatNumbersInAListSizeXthatEnumerateToAnIntegerSizeN(self):
        return [np.round(i,2) for i in np.random.dirichlet(np.ones(8),size=1)[0]]

    def generateDescription(self):
        return '''
        {} : {}
        {} : {}
        {} : {}
        {} : {}
        {} : {}
        {} : {}
        {} : {}
        '''.format(
            self.resultList[0][0],
            self.resultList[0][1],
            self.resultList[1][0],
            self.resultList[1][1],
            self.resultList[2][0],
            self.resultList[2][1],
            self.resultList[3][0],
            self.resultList[3][1],
            self.resultList[4][0],
            self.resultList[4][1],
            self.resultList[5][0],
            self.resultList[5][1],
            self.resultList[6][0],
            self.resultList[6][1],
            self.resultList[7][0],
            self.resultList[7][1]
        )



