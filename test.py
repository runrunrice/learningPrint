#import numpy as np
#import pandas as pd
#import openpyxl as oppx
#from openpyxl import Workbook
#import csv
#import re
#
#FILE = "D:/売上仕入計上/temp/processing.xlsx"
#RPA = "D:/売上仕入計上/RPA.xlsx"
#RESULTPATH = "D:/売上仕入計上/Result/"
#reader = pd.ExcelFile(FILE)
#for sName in reader.sheet_names:
    #get Nomber of project
#    s = re.search(r"【\d+】",sName)
#    if s:
#        print(s.group(0))#No✔
####print(np.__version__)
#b = list()

#how to input function in cell(use openpyxl)
import urllib.request
x = r'https://cdndoc.pcs.baidu.com/rest/2.0/docview/doc?datatype=pic&dp_logid=375420431553222053&expires=24h&fid=1681551055-250528-355909034054226&method=data&nf=1&object=d5a8ef758821e79acce0689a3641efae&rt=sh&sign=FOTRE-DCb740ccc5511e5e8fedcff06b081203-uSXRHzFXL688Vi87G9qNVLeLIGc%253D&timestamp=1636598756&pagenum='

for i in range(13,694):
    u=x+str(i)
    request = urllib.request.Request(u)
    response = urllib.request.urlopen(request)
    img = response.read()
    with open("d:/reading/"+str(i)+".png", "wb") as f:
        f.write(img)

"""
def a(x):
    x[2]=3

def main():
    aa=[1,1,1,1,1]
    print(aa[2])
    a(aa)
    print(aa[2]) 


main()
"""

"""
book = Workbook()
sheet = book.active
sheet["B2"] = 56
sheet["C3"] = "=B2+1"
print(sheet["C3"].value)
"""
