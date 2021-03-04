from threading import Thread

import numpy as np

from Assets.lib.ImageFormatter import cropImageByColorDetection, resizeImage


class Tensorflow():
    def __init__(self):
        Thread(target=self.finishInit,daemon=True).start()
    def finishInit(self):
        pass
        #self.model = tf.keras.models.load_model(Directories().model)

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