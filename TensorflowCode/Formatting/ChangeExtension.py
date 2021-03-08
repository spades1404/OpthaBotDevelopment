from os import listdir
from os.path import isfile, join
import os
import string
import  random
from PIL import Image
mypath = r"C:\Users\rajib\Documents\OBNewDataset\REMAKE\stare"

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in files:
    x = os.path.join(mypath,i)
    f = Image.open(x)

    f.save(os.path.join(mypath,f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=7))}.jpg"))
    os.remove(x)
