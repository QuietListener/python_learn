week_day = 6

if week_day == 6:
    print("周六睡个觉")
elif week_day == 7:
    print("继续睡觉")
elif week_day == 3:
    print("去浪一浪")
else:
    print("好好干活")


value = 3
b1 = value == 3
b2 = value == 4
print(str(b1))
print(str(b2))


i = 0;
while i < 3:
    print(str(i))
    i = i+1;

count = 1
while count <= 10:
    print(str(count)+" 你好，我好无聊")
    count+=1


dict_student = {2020101:"李雷",2020202:"韩美美",2020303:"小明"}
dict_student



def printWords():
    count = 1
    while count <= 10:
        print(str(count)+" 你好，我好无聊")
        count+=1

printWords()
printWords()


class Bird:
     '''鸟类'''

     def __init__(self, name):
            '''每当创建新实例时候，python会自动运行
                self是一个指向实例本身的引用
                每一个类方法都有指向
            '''
            self.name = name;

     def eat(self):
         '''鸟类可一吃东西'''
         print(self.name + " is eating")

     def fly(self):
         '''鸟在飞'''
         print(self.name+" is  am flying")

     def getName(self):
         '''获取你鸟儿的名'''
         self.aa = "lala"
         return self.name

b1 = Bird("windy")
b2 = Bird("老鸟")

b1.eat()
b2.eat()
b1.fly()
b2.fly()
print(b1.name)
print(b2.name)


print(True)
print(1)

s = "abd "
#s1 = s + 1;
#print(s1)

print(s == 1)
print("aaaaa")

# s1 = "我有"
# value = 1000
# s2 = "万"
#
# s3 = s1 + value + s2

b = True
s4 = "我有1000万是"+str(b)+"的"
print(s4)
