from __future__ import absolute_import, division, print_function, unicode_literals
import plaidml.keras
import os
plaidml.keras.install_backend()
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
print(os.environ["KERAS_BACKEND"])
import sklearn
import random
import numpy as np
import tempfile
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import tensorflow as tf

from keras.models import Model
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Activation, Flatten, Dense, Dropout, Reshape, ZeroPadding2D,BatchNormalization,AveragePooling2D,Add,Input
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam,RMSprop
from keras import activations
from keras.callbacks import EarlyStopping
from keras.regularizers import l2

import os

global IMG_SIZE, NB_CHANNELS, BATCH_SIZE,NB_TRAIN_IMAGE,NB_VALID_IMG, WEIGHTS,DATALOC


DATALOC = r"C:\Users\rajib\Documents\GitHub\OpthaBotDevelopment\TensorflowCode\Formatting\data"
IMG_SIZE = 227# Replace with the size of your images
NB_CHANNELS = 3 # 3 for RGB images or 1 for grayscale images
BATCH_SIZE = 16 # Typical values are 8, 16 or 32
NB_TRAIN_IMG = sum([len(files) for r, d, files in os.walk(os.path.join(DATALOC,"train"))]) # Replace with the total number training images
NB_VALID_IMG = sum([len(files) for r, d, files in os.walk(os.path.join(DATALOC,"validation"))]) # Replace with the total number validation images
WEIGHTS = None #Weighting for number of data in dataset class

print(NB_TRAIN_IMG)
print(NB_VALID_IMG)


def makeGenerators(dataLoc):
    # Creating data generators

    train_datagen = ImageDataGenerator(
        width_shift_range=0.1,
        height_shift_range=0.25,
        rescale=1. / 255,
        shear_range=0.05,
        zoom_range=0.1,
        horizontal_flip=True)

    validation_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        fr'{dataLoc}\train',
        batch_size=BATCH_SIZE,
        target_size=(IMG_SIZE, IMG_SIZE),
        class_mode="categorical")

    validation_generator = validation_datagen.flow_from_directory(
        fr'{dataLoc}\validation',
        batch_size=BATCH_SIZE,
        target_size=(IMG_SIZE, IMG_SIZE),
        class_mode="categorical")


    print(train_generator.class_indices)

    weights = sklearn.utils.class_weight.compute_class_weight("balanced",np.unique(train_generator.classes),train_generator.classes)

    return train_generator,validation_generator, weights

def generateModel1():
    model = Sequential(
        [
            Conv2D(filters=128,kernel_size = (2,2),strides=(1,1),padding="same",data_format="channels_last",input_shape=(IMG_SIZE,IMG_SIZE,NB_CHANNELS),activation="relu"),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            MaxPooling2D(pool_size=(2,2)),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            Conv2D(filters=128, kernel_size=(2, 2), strides=(1, 1), padding="valid", activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Flatten(),
            Dense(64,activation="relu"),
            Dense(8,activation="softmax")
        ]
    )
    model.compile(loss = "categorical_crossentropy",optimizer="RMSprop",metrics=["accuracy"])

    print(model.summary())
    return model

def legacyModel():
    model = keras.models.Sequential(  # Creating Model Object
        [
            Conv2D(filters=96,kernel_size = (2,2),strides=(1,1),padding="same",data_format="channels_last",input_shape=(IMG_SIZE,IMG_SIZE,NB_CHANNELS),activation="relu"),
            keras.layers.Conv2D(activation="relu", filters=96, kernel_size=(4, 4)),
            keras.layers.Conv2D(activation="relu", filters=96, kernel_size=(3, 3)),
            keras.layers.Conv2D(activation="relu", filters=96, kernel_size=(2, 2)),
            keras.layers.MaxPool2D(pool_size=(2, 2)),  # This reduces the image, by averaging 16 pixles down to 4
            keras.layers.Conv2D(activation="relu", filters=64, kernel_size=(4, 4)),
            keras.layers.Conv2D(activation="relu", filters=64, kernel_size=(3, 3)),
            keras.layers.Conv2D(activation="relu", filters=64, kernel_size=(2, 2)),
            keras.layers.MaxPool2D(pool_size=(2, 2)),  # This reduces the image, by averaging 16 pixles down to 4
            keras.layers.Conv2D(activation="relu", filters=128, kernel_size=(4, 4)),
            keras.layers.Conv2D(activation="relu", filters=128, kernel_size=(3, 3)),
            keras.layers.Conv2D(activation="relu", filters=128, kernel_size=(2, 2)),
            keras.layers.MaxPool2D(pool_size=(2, 2)),  # This reduces the image, by averaging 16 pixles down to 4
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(4, 4)),
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(3, 3)),
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(2, 2)),
            keras.layers.MaxPool2D(pool_size=(2, 2)),  # This reduces the image, by averaging 16 pixles down to 4
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(4, 4)),
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(3, 3)),
            keras.layers.Conv2D(activation="relu", filters=256, kernel_size=(2, 2)),
            keras.layers.Flatten(),  # Flattens our input vector
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(8,activation="softmax")
        ]
    )

    print(model.summary())
    model.compile(optimizer='SGD',
                  loss="categorical_crossentropy",
                  metrics=['accuracy'])

    return model

def alexNet(optimizer = "adam"):


    model = keras.models.Sequential([
        keras.layers.Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu',input_shape=(227, 227, 3)),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
        keras.layers.Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
        keras.layers.Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(filters=384, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(filters=256, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(4096, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(4096, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(7, activation='softmax')
    ])

    print(model.summary())
    model.compile(optimizer='adam',
                  loss="categorical_crossentropy",
                  metrics=['accuracy'])

    return  model



def fit(model,savename = "model.h5"):
    model.fit_generator(
        t,
        steps_per_epoch=NB_TRAIN_IMG // BATCH_SIZE,
        epochs=100,
        validation_data=v,
        validation_steps=NB_VALID_IMG // BATCH_SIZE,
        callbacks=[es],
        class_weight=WEIGHTS
    )
    model.save(savename)
if __name__ == "__main__":
    global es
    es = keras.callbacks.EarlyStopping(monitor="val_acc",patience=10,mode="max",restore_best_weights=True)

    t,v,WEIGHTS = makeGenerators(DATALOC)

    #AlexNet with Adam
    m = alexNet("adam")
    fit(m,savename="ALEXNETADAM2.h5")

    print("done")
