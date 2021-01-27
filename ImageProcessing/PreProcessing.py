##THIS FILE WILL HANDLE DATA PRE MODEL INIT DATA PROCESSING - CONVERTING IMAGES INTO A FORMAT THAT THE MODEL CAN UNDERSTAND EASILY##
import numpy as np
import random
from PIL import ImageOps
from DataGrabbing.DataFormatting import generateStructures
import tensorflow as tf

def twoD2threeD(array): #Converts a 2d flat array into a 3d array
    return np.reshape(list(array.getdata()), (256, 256, 3)).tolist()

def nparray2list(array): #CONVERT 3D NUMPY ARRAY INTO A LIST
    return [np.array(i).tolist() for i in array]

def enlargeDataset(data,labels):
    data += [ImageOps.mirror(i) for i in data]
    labels += labels

    return data, labels

def oneHotEncode(num): #this converts our labels into one hot format
    switcher = { #im just hard coding it in to save on clock cycles
        0 : [1,0,0,0,0,0,0,0],
        1 : [0,1,0,0,0,0,0,0],
        2 : [0,0,1,0,0,0,0,0],
        3 : [0,0,0,1,0,0,0,0],
        4 : [0,0,0,0,1,0,0,0],
        5 : [0,0,0,0,0,1,0,0],
        6 : [0,0,0,0,0,0,1,0],
        7 : [0,0,0,0,0,0,0,1]
    }
    return np.array(switcher.get(num))

def linkedShuffler(a,b): #shuffles two lists without disturbing the relationships
    c = list(zip(a,b))
    random.shuffle(c)
    a,b = zip(*c)
    return a,b


def returnTensorDataset(sheet,pics,index=50): #Takes the location of where the spread sheet is and where the pictures are
    print("Unpacking Data")
    images, labels = generateStructures(sheet, pics, index)
    images, labels = enlargeDataset(images, labels)
    images,labels = linkedShuffler(images,labels) #SHUFFLING
    #formatting the bulk data

    print("Formatting Data")
    images = np.array([np.array(i) for i in images])
    labels = tf.keras.utils.to_categorical(labels,num_classes=None,dtype="uint8")

    print("Splitting Data")
    listSlice = round(len(images)*0.9)  # Decides how much of our data will be reserved for testing and how much for training.


    print(listSlice)
    return  images[0:listSlice],labels[0:listSlice],images[listSlice:-1],labels[listSlice:-1] #This slices our full set into training and test data

if __name__ == "__main__":

    print(linkedShuffler([1,2,3],["a","b","c"]))


