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



#函数返回值
def format_name(first_name,last_name):
    full_name = first_name +" "  + last_name
    return full_name

fname = format_name("andy","yang")
print(fname)

#返回多个值
def return_tuple(v1,v2,v3):
    return v1,v2,v3

r1 = return_tuple(1,2,3)
print(r1)

rr1,rr2,rr3 = return_tuple(2,3,4)
print(rr1,rr2,rr3)

# 任意数据量的参数
def make_pizza(*toppings):
    '''topings是一个tupe'''
    print(toppings)

make_pizza("a","b","c")


# 结合位置实参和任意数量的实参
def make_pizza1(size,*toppings):
    '''topings是一个tupe'''
    print(str(size))
    print(toppings)

make_pizza1(12,"a","b")

# 任意数量的关键字实参

'''
**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所
有名称—值对都封装到这个字典中。
'''
def build_profile(first,last,**userinfo):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in userinfo.items():
        profile[key] = value;
    return profile;

profile = build_profile("andy","yang",location="princeton",field="physics")
print(profile)