from openpyxl import Workbook
import time
import random
for i in range(1,5):
    print(i)

    book = Workbook()
    sheet = book.active

    sheet['A' + str(1)] = "学号"
    sheet['B' + str(1)] = "语文"
    sheet['c' + str(1)] = "数学"
    sheet['d' + str(1)] = "英语"
    sheet['e' + str(1)] = "理科综合"
    sheet['f' + str(1)] = "总分"

    count = 2
    while count < random.randint(40,55) :
        sheet['A'+str(count)] = 20203000+100*i+count
        yuwen = random.randint(60,random.randint(120,140))
        shuxue = random.randint(80,random.randint(130,150))
        yingyu = random.randint(90,147)
        zonghe = random.randint(160,296)
        sheet['B'+str(count)] = yuwen
        sheet['c' + str(count)] = shuxue
        sheet['d' + str(count)] = yingyu
        sheet['e' + str(count)] = zonghe
        sheet['f' + str(count)] = yuwen+shuxue+yingyu+zonghe
        count+=1

    book.save("高三"+str(i)+"班.xlsx")