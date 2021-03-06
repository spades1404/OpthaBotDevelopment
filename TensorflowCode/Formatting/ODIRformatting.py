import openpyxl as px
import ast
import shutil

IMAGEDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\odir\preprocessed_images"
SHEETDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\odir\full_df.xlsx"
OUTPUTDIRECTORY = r"C:\Users\rajib\Documents\OBNewDataset\SORTED"

NORMAL = "normal fundus"
RANGE = 3195


W = px.load_workbook(SHEETDIRECTORY)
p = W.get_sheet_by_name(name = "full_df")

leftImages = [p['D%s'%i].value for i in range(2,RANGE)]
rightImages = [p['E%s'%i].value for i in range(2,RANGE)]

leftDiag = [p['F%s'%i].value for i in range(2,RANGE)]
rightDiag = [p['G%s'%i].value for i in range(2,RANGE)]

truth = [ast.literal_eval(i) for i in [p['R%s'%i].value for i in range(2,RANGE)]]

for i in range(len(truth)):
    t = truth[i]
    ld = leftDiag[i]
    rd = rightDiag[i]
    li = leftImages[i]
    ri = rightImages[i]
    #print(t)


    '''
    print(t)
    print(ld)
    print(rd)
    print(li)
    print(ri)
    '''

    diag = t.index(1)
    #print(diag)

    try:

        if diag == 0:
            shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")

        elif diag == 1:
            if NORMAL in ld:

                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\2\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\2\{ri}")


        elif diag == 2:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\3\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\3\{ri}")

        elif diag == 3:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\4\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\4\{ri}")

        elif diag == 4:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\5\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\5\{ri}")

        elif diag == 5:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\6\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\6\{ri}")

        elif diag == 6:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\7\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\7\{ri}")

        elif diag == 7:
            if NORMAL in ld:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\1\{li}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{li}", fr"{OUTPUTDIRECTORY}\8\{li}")

            if NORMAL in rd:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\1\{ri}")
            else:
                shutil.copyfile(fr"{IMAGEDIRECTORY}\{ri}", fr"{OUTPUTDIRECTORY}\8\{ri}")

    except Exception as e:
        print(e)








