import openpyxl #导入openpyxl模块，用于操作excel

ave_dict = {}
for i in range(1,5):

    name = "sample"+str(i)+".xlsx";
    book = openpyxl.load_workbook(name) #打开xlsx文件，方便后面读取
    sheet = book.active

    count = 0
    total = 0

    while True:
        score = sheet['f' + str(count+2)].value
        if score  == None:
            break;

        total+=score
        count+=1

    print("total="+str(total) +" count="+str(count))
    ave = total/count;
    print("average="+str(ave))
    ave_dict[name] = ave;
    book.close

print(ave_dict)
print(sorted(ave_dict.items(), key = lambda kv:(kv[1], kv[0])))
