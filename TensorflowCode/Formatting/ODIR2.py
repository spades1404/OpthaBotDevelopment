import openpyxl as px
import ast
import os
import shutil

IMAGEDIR = r"C:\Users\rajib\Documents\OBNewDataset\REMAKE\odir\IMAGES"
SHEET = r"C:\Users\rajib\Documents\OBNewDataset\REMAKE\odir\datad.xlsx"
OUTPUT = r"C:\Users\rajib\Documents\OBNewDataset\REMAKE\odir\testarea2"
RANGE = 3502


W = px.load_workbook(SHEET)
p = W.get_sheet_by_name(name = "Sheet1")

leftImages = [p['D%s'%i].value for i in range(2,RANGE)]
rightImages = [p['E%s'%i].value for i in range(2,RANGE)]

verboseLeft = [p['F%s'%i].value for i in range(2,RANGE)]
verboseRight = [p['G%s'%i].value for i in range(2,RANGE)]

des1 = [p['H%s'%i].value for i in range(2,RANGE)]
des2 = [p['I%s'%i].value for i in range(2,RANGE)]
des3 = [p['J%s'%i].value for i in range(2,RANGE)]
des4 = [p['K%s'%i].value for i in range(2,RANGE)]
des5 = [p['L%s'%i].value for i in range(2,RANGE)]
des6 = [p['M%s'%i].value for i in range(2,RANGE)]
des7 = [p['N%s'%i].value for i in range(2,RANGE)]
des8 = [p['O%s'%i].value for i in range(2,RANGE)]

overall = [list(a) for a in zip(des1,des2,des3,des4,des5,des6,des7,des8)]
desc = ["normal fundus","retinopathy","glaucoma","cataract","macular degeneration","hypertensive retinopathy","myopia"]

for i in range(3500):
    li = leftImages[i]
    ri = rightImages[i]
    o = overall[i]

    ld = verboseLeft[i]
    rd = verboseRight[i]


    '''
    print(li)
    print(ri)
    print(o)
    

    for k in range(8):
        if o[k] == 1:
            shutil.copyfile(os.path.join(IMAGEDIR,li),os.path.join(OUTPUT,str(k),li))
            shutil.copyfile(os.path.join(IMAGEDIR,ri), os.path.join(OUTPUT,str(k), ri))
    '''

    leftCheck = False
    rightCheck = False

    lc = 0
    rc = 0
    for k in desc:

        if k in ld:
            #shutil.copyfile(os.path.join(IMAGEDIR, li), os.path.join(OUTPUT, str(desc.index(k)), li))
            leftCheck = True
            lc +=1

        if k in rd:
            #shutil.copyfile(os.path.join(IMAGEDIR, ri), os.path.join(OUTPUT, str(desc.index(k)), ri))
            rightCheck = True
            rc +=1

    if lc > 1:
        print(lc)
    if rc > 1:
        print(rc)

    if leftCheck == False:
        shutil.copyfile(os.path.join(IMAGEDIR, li), os.path.join(OUTPUT, str(7), li))
    if rightCheck == False:
        shutil.copyfile(os.path.join(IMAGEDIR, ri), os.path.join(OUTPUT, str(7), ri))
    #print(f"Done with {i}")




