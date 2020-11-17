#字符串相等
v = "a"
print(v=="a")
print(v=="A")

#数字相等
v1 = 1
print(v1==1)
print(v1 == 2)
print(v1>=2)

#多个条件
v2 = 3
print(v1 == 1 and v2 == 2)
print(v1 == 1 or v2 == 2)

#是否在列表中
l1 = ["a","b",1,2]
print(1 in l1)
print(3 in l1)
print(3 not in l1) #true

'''
if condition 9_test:
   do something
'''

v3 = 1
if v3 == 1:
    print("v3 is 1")


if v3 == 2:
    print("v3 is 1")
else:
    print("v3 is not 1")


v4 = 15
if v4 < 12:
    print("v4 is less than 12")
elif v4 <18:
    print("v4 is between 12 and 18")
else:
    print("v4 is morethan 18")


l2 = []
if not l2:
    print("l2 is empty")


# 取模 余数
print(4%3)
print(5%3)



'''
while
'''

#whiel
num = 1
while num<5:
    print(num)
    num+=1



#while break;
while True:
    city = input("city:")
    if city == "quit":
        break
    else:
        print("welcome to "+city)

#while continue
num = 0
while num < 10:
    num+=1
    if num > 5:
        continue;
    print("num")




#while 列表
pets = ['dog','cat','cat','rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


'''
input
'''
# 输入
name = input("you name:")
print("\r\nhello:"+ name );

age = input("age:")
age = int(age)
if age > 18:
    print("你是成年人")
else:
    print("小屁孩你好")




