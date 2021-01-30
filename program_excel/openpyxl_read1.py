import openpyxl #导入openpyxl模块，用于操作excel

name = "高三1班"
file_name = name+".xlsx" #文件名
book = openpyxl.load_workbook(file_name) #打开xlsx文件，方便后面读取
sheet = book.active #得到默认的sheet
print(sheet["A1"].value) #第A列第1行的内容
print(sheet["B1"].value) #第B列第1行的内容
print(sheet["B3"].value) #第B列第3行的内容
print(sheet["F2"].value) #第F列第2行的内容