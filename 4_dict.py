#字典
d = {"a":12, "b":"bbb"}
print(d)

#访问字典
print(d["a"])

#添加 修改
d["c"]="ccc"
d["a"] = "aaa"
print(d)


# 不能重复
# d1 = {"a":1,"a":2}
# print d1

#删除
print("before del:"+str(d))
del d["a"]
print("after del:"+str(d))

#遍历
users = {"junjun":12,"laowang":40}
for key,value in users.items():
    print("key:"+key+ "value:"+str(value))

print("only name")
for name in users.keys():
    print("name:"+name)