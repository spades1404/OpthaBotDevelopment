from threading import Thread
from keras.preprocessing import image as KIMG
import numpy as np

from Other.ImageFormatter import cropImageByColorDetection, resizeImage

from Class.globalF import globalFuncs
import tensorflow as tf


class Tensorflow():
    def __init__(self):
        self.model = tf.keras.models.load_model(globalFuncs.directories.model)

    def analyzeImageVerbose(self, dir):
        try:
            image = cropImageByColorDetection(dir)  # Crops the image to the required content
        except:
            print("Initial Crop Failed - Perhaps the image is not colour?")
            return
        # reduce image
        image = resizeImage(image, dim=256)

        # convert to matrix
        image = np.array(image)
        matrix = np.array([image])

        print(self.model.predict(matrix))

        return(list(list(self.model.predict(matrix))[0]))

    def Image2MatrixWithKeras(self,img): #Takes file location
        img = KIMG.load_img(img, target_size=(227, 227))
        img = KIMG.img_to_array(img) / 255.
        img = np.expand_dims(img, axis=0)
        return img


    def analyzeImageSuccinct(self,image):
        matrix = self.Image2MatrixWithKeras(image)

        print(self.model.predict(matrix))

        return [round(val.item(),2) for val in (list(list(self.model.predict(matrix))[0]))]




if __name__ == "__main__":
    Tensorflow()