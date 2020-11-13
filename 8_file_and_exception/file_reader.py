#使用with会自动关闭文件
with open("data.text") as file_obj:
    content = file_obj.read() #读取所有
    print(content)


#逐行读取
with open("data.text") as file_obj:
    for line in file_obj:
        print(line.rstrip())

#读取到一个列表
with open("data.text") as file_obj:
    lines = file_obj.readlines()

print(lines)



#写文件
filename = "programming.txt"
with open(filename,"w") as file_obj:
    file_obj.write("i love programming");

#附加文件
with open(filename,"a") as file_obj:
    file_obj.write("i love programming too");


'''
异常
'''
d = 1
try:
    answer = 1/d
    print(answer)
except ZeroDivisionError:
    print("you can't divide by 0")
else: #依赖于try代码块成功执行的代码都应放到else代码块中
    print(answer)



#异常时候一声不吭
try:
    answer = 1/0
    print(answer)
except ZeroDivisionError:
   pass #什么都不做
else: #依赖于try代码块成功执行的代码都应放到else代码块中
    print(answer)


