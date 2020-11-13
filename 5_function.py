def greet_user():
    '''显示简单的问候语'''
    print("hello")


greet_user()

def greet_user(user_name):
    print("hello:"+str(user_name))

greet_user("junjun");


def modify(value):
    value="111"

v = "222"
modify(v)
print(v)


#参数
def hello(name,words="no comment"):
    print("hello "+ name+" ,"+ words)

hello("junjun","you do well")#位置实参
hello(words="you do bad",name="andy") #关键字实参
hello("junjun") #默认实参