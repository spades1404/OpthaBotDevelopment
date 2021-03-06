import openpyxl as px
import ast
import shutil
import os

IMAGEDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\drdc\resized_train\resized_train"
SHEETDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\drdc\trainLabels.xlsx"
OUTPUTDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\SORTED"

RANGE = 35127

W = px.load_workbook(SHEETDIRECTORY)
p = W.get_sheet_by_name(name = "trainLabels")

images = [f"{i}.jpeg" for i in [p['A%s'%i].value for i in range(2,RANGE)]]
labels = [int(i) for i in [p['B%s'%i].value for i in range(2,RANGE)]]

for i in range(len(images)):
    im = images[i]
    lb = labels[i]

    if lb == 0:

        shutil.copyfile(fr"{IMAGEDIRECTORY}\{im}",fr"{OUTPUTDIRECTORY}\1\{im}")
        #os.remove(fr"{OUTPUTDIRECTORY}\1\{im}")

    elif lb == 1:
        shutil.copyfile(fr"{IMAGEDIRECTORY}\{im}",fr"{OUTPUTDIRECTORY}\2\{im}")
        #os.remove(fr"{OUTPUTDIRECTORY}\2\{im}")
