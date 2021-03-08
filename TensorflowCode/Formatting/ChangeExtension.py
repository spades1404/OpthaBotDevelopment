from os import listdir
from os.path import isfile, join
import os
import string
import random
from PIL import Image


def changeindir(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for i in files:
        x = os.path.join(mypath, i)
        try:
            f = Image.open(x)

            f.save(os.path.join(mypath, f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=7))}.jpg"))
            os.remove(x)
            print(f"Complete Conversion for {x}")
        except:
            print(f"Had to delete {x}")
            os.remove(x)


if __name__ == "__main__":
    root = r"/content/drive/MyDrive/Colab Notebooks/datanew"

    changeindir(os.path.join(root, "train", "0"))
    changeindir(os.path.join(root, "train", "1"))
    changeindir(os.path.join(root, "train", "2"))
    changeindir(os.path.join(root, "train", "3"))
    changeindir(os.path.join(root, "train", "4"))
    changeindir(os.path.join(root, "train", "5"))
    changeindir(os.path.join(root, "train", "6"))
    changeindir(os.path.join(root, "train", "7"))

    changeindir(os.path.join(root, "validation", "0"))
    changeindir(os.path.join(root, "validation", "1"))
    changeindir(os.path.join(root, "validation", "2"))
    changeindir(os.path.join(root, "validation", "3"))
    changeindir(os.path.join(root, "validation", "4"))
    changeindir(os.path.join(root, "validation", "5"))
    changeindir(os.path.join(root, "validation", "6"))
    changeindir(os.path.join(root, "validation", "7"))