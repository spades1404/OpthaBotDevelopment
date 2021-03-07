from __future__ import absolute_import, division, print_function, unicode_literals
import random
import tensorflow as tf
from openpyxl import load_workbook
from PIL import Image
from PIL import ImageOps
import numpy as np
import tempfile
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout, Reshape
from keras.preprocessing.image import ImageDataGenerator

import os

IMG_SIZE = 512# Replace with the size of your images
NB_CHANNELS = 3 # 3 for RGB images or 1 for grayscale images
BATCH_SIZE = 32 # Typical values are 8, 16 or 32
NB_TRAIN_IMG = 4530 # Replace with the total number training images
NB_VALID_IMG = 1979 # Replace with the total number validation images

def saveModelh5py(model, VER = 1,MODEL_DIR = None): #VER is the version number of the model - just for keeping track of up to date files
    if MODEL_DIR == None:
        MODEL_DIR = tempfile.gettempdir() #grabs a temporary directory to store the model in
    EXPORT_PATH = os.path.join(MODEL_DIR, str(VER)) #Generates the path we are exporting to

    tf.keras.models.save_model(
        model,
        EXPORT_PATH,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None
    ) #This funtion will save the model for us as a protobuf file - makes it easy to serve it

    print("Saved Model To {}".format(EXPORT_PATH))



def createModel(dataLoc):

    #Creating data generators

    train_datagen = ImageDataGenerator(
        width_shift_range=0.1,
        height_shift_range=0.1,
        rescale=1. / 255,
        shear_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True)

    validation_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        fr'{dataLoc}\train',
        batch_size=32,
        target_size=(IMG_SIZE,IMG_SIZE))
    validation_generator = validation_datagen.flow_from_directory(
        fr'{dataLoc}\validation',
        batch_size=32,
        target_size=(IMG_SIZE,IMG_SIZE))

    print(train_generator.image_shape)
    print(train_generator.num_classes)

    #print(train_generator.image_shape)

    #Defining model

    model = Sequential()

    #model.add(Reshape(input_shape=(512,512,3),target_shape=(1,512,512,3)))

    model.add(
        Conv2D(
            filters=64,
            kernel_size=(2,2),
            strides=(1,1),
            padding="same",
            data_format='channels_last',
            input_shape=(IMG_SIZE,IMG_SIZE,3)
        )
    )
    print(model.input_shape)


    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(
        Conv2D(
            filters=64,
            kernel_size=(2, 2),
            strides=(1, 1),
            padding="valid",
        )
    )

    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(
        Conv2D(
            filters=64,
            kernel_size=(2, 2),
            strides=(1, 1),
            padding="valid",
        )
    )

    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64,activation="relu"))
    model.add(Dropout(0.25))
    model.add(Dense(8))
    model.add(Activation("sigmoid"))

    model.compile(loss = "categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

    model.fit_generator(
        train_generator,
        steps_per_epoch=NB_TRAIN_IMG//BATCH_SIZE,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=NB_VALID_IMG//BATCH_SIZE
    )
    model.save_weights("model.h5")

    saveModelh5py(model)

createModel(r"C:\Users\rajib\Documents\OBNewDataset\data")



