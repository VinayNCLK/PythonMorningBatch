
from utilities.excel_testdata import *
import sys

sheetname ="test_invalidlogin_multipledata"
exceldata_path = sys.path[1]+"//test_data.xlsx"
numberofrows = getnoofrows(exceldata_path,sheetname)
print(numberofrows)

for i in range(2,numberofrows+1):
    print(getcellvalue(exceldata_path,sheetname,rowno=i,colmunno=2))
    print(getcellvalue(exceldata_path, sheetname, rowno=i, colmunno=3))