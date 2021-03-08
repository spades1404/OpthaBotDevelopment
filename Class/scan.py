import random
import string
from datetime import datetime

import numpy as np
from PIL import Image

from Other.ImageFormatter import cropImageByColorDetection, resizeImage
from Class.globalF import globalFuncs
#from Class.algorithm import Tensorflow


class Scan():
    def __init__(self):
        self.imageDirectory = None
        self.result = []
        return
    def initialiseFromProg(self,fileLoc):
        self.scanTime = datetime.now()
        self.fileName = "{}.jpg".format(''.join(random.choices(string.ascii_uppercase + string.digits, k=15)))
        self.originalImage = Image.open(fileLoc)
        self.postProcessImage = self.preProcessImage(fileLoc)

        self.imageDirectory = globalFuncs.directories.temp + self.fileName
        self.postProcessImage.save(fp=self.imageDirectory)
        self.custID = ""
        self.serverID = None




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

    def uploadScanToDatabase(self):
        globalFuncs.database.uploadScan(self)
        return


    def grabImage(self):
        print(globalFuncs.directories.temp)
        self.imageDirectory = globalFuncs.directories.temp + (self.details["location"].split("/")[1])
        globalFuncs.database.downloadFromFirebaseStorage(self.details["location"], self.imageDirectory)

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

        if globalFuncs.appInfo["facade"] == True:
            self.result = self.formatList(self.result)
        print(self.result)
        self.generateMultiDiListofResults()#



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

        self.resultList = sorted(self.resultList, key=lambda x: x[1],reverse=True) #Sort List by probability


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

    def formatList(self,*args):
        return self.indiscriminateFunctionToGenerateRandomFloatNumbersInAListSizeXthatEnumerateToAnIntegerSizeN()

