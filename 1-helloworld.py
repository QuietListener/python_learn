# -*- coding: utf-8 -*-

print("hello world")

#多行
print (r'''
adfad
asdfasdf

afaf
''')
#注释

print("###数据类型和变量###")


#布尔值
print("---布尔值---")
print(2>3 == True)
print(2>3 and False or True)
print(not 1)

#python仲的空
print(None)

print("\n---变量---")
print("\n---变量名只能是字母，数字，下划线，不能将关键字和函数名作为变量名字---")
a = 1
b = "str"
c = True
x=10
x+=2
print(x)

#动态语言~ a从int变为String了
a = "1111"
print(a)


#常量 习惯上用大写字幕开头，但是本质上是变量
PI = 3.14
PI = 123

#除法
print(9/3) #3.0
print(9//3) #3

#使用函数str避免类型错误。
age = 23
name="junjun"
msg = name+" is "+str(age)+ " old"
print(msg)


print("\n###字符串和编码###")
#在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如
print("你好china")
print(len('你好'))#2
print(len('china'))#5

print("\n---格式化---")
print('Hi, %s, you have $%f' % ('Michael', 1000000.11))
print('Hello, {2}, 成绩提升了 {1:.1f}%'.format('小明', 17.125,"小张"))



###数据类型和变量###
print("###list和tuple###")

print("\n---list---")
classmates = ["小张","Mike",123]
print(classmates)
print(len(classmates))
print(classmates[1])
#print(classmates[3]) #IndexError: list index out of range

#负数倒着取
print("---负数倒着取---")
print(classmates[-1])
print(classmates[-2])
classmates.append(True)
print(classmates)

print("\n###tuple###")
#tuple 是一种有序列表；tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
t1 = (1,2)
print(t1)
t2 = () #空tuple
print(t2)

#特变注意下面不是一个tuple
t3 = (3) #这里有一个歧义 小括号可以是tuple也可以是数学上的小括号，python在这里默认取数学上的小括号
print(t3) #3

#一个元素的tuple
t4 = (3,)
print(t4)
print(len(t4))


print("\n---改变tuple---")
t11 = (1,2,[True,3])
print(t11) #(1, 2, [True, 3])
t11[2][1] = False
print(t11) #(1, 2, [True, False])
#----tuple的不便性其实是每个元素指向的内存不便，内存的内容可以变的---






