tip
读取并打印所有人的总分
name
main.py
p
import openpyxl #导入openpyxl模块，用于操作excel

name = "高三1班"
name_file = name+".xlsx"
book = openpyxl.load_workbook(name_file) #打开xlsx文件，方便后面读取
sheet = book.active #得到默认的sheet

row_num = 2 #行号,从第2行开始
total_score = 0 #总分
while True: #循环
    position = 'F' + str(row_num) #定位单元格的位置
    score = sheet[position].value #获取单元格的内容
    if score  == None: #如果单元格的内容是None，就表示下面没有内容了，跳出循环
        break;
    print(position+"的值是:"+str(score)) #打印所有人的总分
    total_score += score #计算总分
    row_num += 1 #跳到下一行

student_count = row_num-2 #学生的人数
ave_score = total_score/student_count #计算平均分 总分/人数

print("学生人数:"+str(student_count))  #打印学生人数
print("平均分:" + str(ave_score)) #打印平均分