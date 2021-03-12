from os import listdir
from os.path import isfile, join
import os
import string
import random
from PIL import Image


def changeindir(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(files)
    for i in files:
        x = os.path.join(mypath, i)
        try:
            f,ext = os.path.splitext(i)
            if ext != ".jpg":
                f = Image.open(x)

                f.save(os.path.join(mypath, f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=7))}.jpg"))
                os.remove(x)
                print(f"Complete Conversion for {x}")
            else:
                continue
        except:
            try:
                os.remove(x)
                print(f"Had to delete {x}")

            except:
                print(f"Damn, not even delete works - {x}")


if __name__ == "__main__":
    root = r"C:\Users\rajib\Documents\OBNewDataset\REMAKE\odir\testarea2"

    changeindir(os.path.join(root, "0"))
    changeindir(os.path.join(root,"1"))
    changeindir(os.path.join(root, "2"))
    changeindir(os.path.join(root, "3"))
    changeindir(os.path.join(root,"4"))
    changeindir(os.path.join(root,"5"))
    changeindir(os.path.join(root,"6"))
    changeindir(os.path.join(root,"7"))
