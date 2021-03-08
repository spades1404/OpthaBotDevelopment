from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

train_datagen = ImageDataGenerator(
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    rescale = 1./255,
    shear_range = 0.1,
    zoom_range = 0.2,
    horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    r'C:\Users\rajib\Documents\GitHub\OpthaBotDevelopment\TensorflowCode\Formatting\datanew\train',
    batch_size=32,
    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(
    r'C:\Users\rajib\Documents\GitHub\OpthaBotDevelopment\TensorflowCode\Formatting\datanew\validation',
    batch_size=32,
    class_mode='binary')