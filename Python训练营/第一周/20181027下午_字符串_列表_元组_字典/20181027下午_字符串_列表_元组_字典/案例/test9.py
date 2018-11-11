dic = {"姓名":"关羽","年龄":30,"邮箱":"guanyu@163.com","武器":"青龙偃月刀"}
"""
for v in dic.keys():
	print(v)
"""
"""
for v in dic.values():
	print(v)
"""
"""
for v in dic.items():
	print(v)
"""
print(dic["年龄"])
print(dic.get("abc"))
dic.pop("姓名")#根据key删除字典中的元素
print(dic)