import openpyxl #导入openpyxl模块，用于操作excel

#定义一个函数计算一个班大于600的人数
def get_more_than_600(name_file):
    book = openpyxl.load_workbook(name_file) #打开xlsx文件，方便后面读取
    sheet = book.active #得到默认的sheet

    row_num = 2 #行号,从第2行开始
    count_600 = 0 #总分大于600的人数

    while True: #循环
        position = 'F' + str(row_num) #定位单元格的位置
        score = sheet[position].value #获取单元格的内容
        if score  == None: #如果单元格的内容是None，就表示下面没有内容了，跳出循环
            break;

        if score >= 600: #计算大于600的人数
            count_600+=1
        row_num += 1 #跳到下一行

    return count_600 #返回大于600分的人数

#计算每个班级的平均分
for i in range(1,5):
    name = "高三"+str(i)+"班"
    name_file = name+".xlsx" #文件名字
    count = get_more_than_600(name_file) #调用函数计算某个班的大于600分的人数
    print(name+" 大于或等于600分的人数: " + str(count)) #打印大于600的人数