from PIL import Image

def checkImage(source):
    try:
        Image.open(source)  # Try and open the image
        return True
    except:
        return False


#Legit Image File
print(checkImage("test.jpeg"))

#Text File
print(checkImage("test.txt"))

#Empty String
print(checkImage(""))

#Fake Location
print(checkImage("fake.txt"))