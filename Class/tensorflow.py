from threading import Thread

import numpy as np

from Other.ImageFormatter import cropImageByColorDetection, resizeImage

from Class.globalF import globalFuncs


class Tensorflow():
    def __init__(self):
        Thread(target=self.finishInit,daemon=True).start()
    def finishInit(self):
        import tensorflow as tf
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

    def analyzeImageSuccinct(self,image):
        image = np.array(image)
        matrix = np.array([image])

        print(self.model.predict(matrix))

        return (list(list(self.model.predict(matrix))[0]))




if __name__ == "__main__":
    Tensorflow()