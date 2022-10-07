import os
import pandas as pd

path = r'C:\Users\User\Desktop\testtask'
fileList = []

class readFiles:
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                fileList.append(os.path.join(root, file))
                print(os.path.join(root, file))
    except:
        pass

class writeToExcel:
    try:
        File = pd.DataFrame(fileList, columns = ['file'], index = range(0, len(fileList)))
        File.to_excel(path + r'\res' + "ult.xlsx", index = False)
    except:
        pass