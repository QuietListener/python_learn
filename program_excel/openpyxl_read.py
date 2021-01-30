import openpyxl #导入openpyxl模块，用于操作excel

dict_ave = {}
dict_600 = {}
for i in range(1,5):

    name = "高三"+str(i)+"班"
    name_file = name+".xlsx"
    book = openpyxl.load_workbook(name_file) #打开xlsx文件，方便后面读取
    sheet = book.active #得到默认的sheet

    count = 0
    total = 0
    count_600 = 0;
    while True:
        score = sheet['f' + str(count+2)].value
        if score  == None:
            break;

        if score >= 600:
            count_600+=1;

        total+=score
        count+=1

    print("total="+str(total) +" count="+str(count))
    ave = total/count;
    print("average="+str(ave))
    dict_ave[name] = ave;
    dict_600[name] = count_600
    book.close

print(dict_ave)
print(dict_600)
total_600 = 0;
for item in dict_600.items():
    total_600 += item[1];

print("大于600分的人数是:"+ str(total_600));





book = openpyxl.Workbook()
sheet = book.active

sheet['A' + str(1)] = "班级"
sheet['B' + str(1)] = "平均分"
sheet['c' + str(1)] = "大于600分人数"

count = 1
while count <= len(dict_ave):
    name = "高三"+str(count)+"班"

    sheet['A' + str(count+1)] = name
    sheet['B' + str(count+1)].value = dict_ave[name]
    sheet['c' + str(count+1)].value = dict_600[name]
    count += 1

sheet['B' + str(count+1)].value = "总人数"
sheet['c' + str(count+1)].value = total_600
book.save("统计结果.xlsx")
