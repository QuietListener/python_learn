
'''
列表由一系列按特定顺序排列的元素组成
用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
'''

#建立列表
l1 = [1,2,"a"]
print(l1)

#访问列表
print(l1[1])

#修改列表元素
l1[0]=10
print(l1)

#添加元素
l1.append("b")
print(l1)

#插入列表
l1.insert(0,-1)
print(l1)

#删除列表
del l1[0]
print(l1)


#删除并获取元素
l1item = l1.pop()
print(l1item)
print(l1)

#删除并获取任意位置元素
l1item = l1.pop(0)
print(l1item)
print(l1)

#按照值来删除
l2 = [1,2,3,1,2,3,1]
print(l2)
l2.remove(2)
print(l2)


#永久排序
l3 = ["baar",'bcnana','cat','apple']
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)

#临时排序
l4 = ['b','c',"a",'d']
l4_1 = sorted(l4)
print(l4)
print(l4_1)

#反转
l5 = ['e','c',"a",'d']
l5.sort()
print(l5)
l5.reverse()
print(l5)

#列表长度
print(len(l5))


print("\n============列表操作============\n")
#遍历整个列表
ll1 = ["good","bad","yes"]
for item in ll1:
    print(item)

print("over")


#创建数值列表
for item in range(1,5):
    print(item)

ll2 = list(range(1,5))
print(ll2)

ll2 = list(range(1,5,2)) #缩进为2
print(ll2)


# 对数字进行简单统计
digits = [1,2,3,4,4,2,6,1]
m1 = max(digits)
m2 = min(digits)
s = sum(digits)
print(m1)
print(m2)
print(s)


#列表解析
ll3 = range(1,5)
ll3_1 = [item +1 for item in ll3]
print(ll3_1)




#使用列表的一部分 切片
ll4 = ['a','b','c','d']
ll4_1 = ll4[1:3]
print(ll4_1)

ll4_2 = ll4[:3]
print(ll4_2)

ll4_3 = ll4[2:]
print(ll4_3)

ll4_4 = ll4[-2:] #最后2个
print(ll4_4)
