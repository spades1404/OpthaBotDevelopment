import numpy as np
import tensorflow as tf
from PIL import Image
from keras.preprocessing import image

MODELLOC = r"model2.h5"

model = tf.keras.models.load_model(MODELLOC)

def returnImageMatrix(img):
    img = Image.open(img)
    img = np.array([np.array(img)])
    #img.reshape((512,512,3))
    print(img.shape)
    return img

def returnWithKeras(img):
    img = image.load_img(img,target_size=(512,512))
    img = image.img_to_array(img)/255.
    img = np.expand_dims(img,axis=0)
    return img

#matrix = returnImageMatrix(r"pigmentaryglaucoma.jpg")
matrix = returnWithKeras(r"dbret.jpg")
x = model.predict(matrix)
print(list(list(x)[0]))


