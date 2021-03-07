import numpy as np
import tensorflow as tf

MODELLOC = ""

model = tf.keras.models.load_model(MODELLOC)

def returnImageMatrix(img):
    return np.array([np.array(img)])

matrix = returnImageMatrix("")

print(model.predict(matrix))


