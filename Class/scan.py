from datetime import datetime
from PIL import Image
from ImageProcessing.ImageFormatter import cropImageByColorDetection, resizeImage
from Class.globalF import globalFuncs
import random
import string
import numpy as np
class Scan():
    def __init__(self,fileLoc):
        # may add validation here instead later
        self.location = fileLoc
        self.scanTime = datetime.now()
        self.originalImage = Image.open(fileLoc)
        self.postProcessImage = self.preProcessImage(self.location)
        self.fileName = r"{}.jpg".format(''.join(random.choices(string.ascii_uppercase + string.digits, k=15)))
        self.custID = None
        self.serverID = None
        self.uploaded = False



    def preProcessImage(self,loc):
        image = cropImageByColorDetection(loc)  # Crops the image to the required content
        image = resizeImage(image,dim=256)
        return image

    def analyze(self): #this func takes a while
        #self.result = Tensorflow().analyzeImageSuccinct(self.postProcessImage)
        self.result = self.indiscriminateFunctionToGenerateRandomFloatNumbersInAListSizeXthatEnumerateToAnIntegerSizeN()
        print(self.result)
        self.generateMultiDiListofResults()
    def generateTemp(self):
        self.postProcessDir = globalFuncs.directories.temp + self.fileName
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








