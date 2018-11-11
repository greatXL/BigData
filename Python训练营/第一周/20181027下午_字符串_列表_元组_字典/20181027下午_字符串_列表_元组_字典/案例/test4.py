#字符串和列表之间的转换
#字符串转列表
s1 = "HelloWorld"
l1 = list(s1)
print(l1)

#列表转字符串
l2 = ["Sheldon","Penny", "Lanard","James"]
s2 = str(l2)
print(s2)

#列表转字符串，需求：SheldonPennyLanardJames
s = ""
for v in l2:
	s += v
print(s)

#列表转字符串，需求：Sheldon,Penny,Lanard,James
s = ""
for v in l2:
	s = s + v + ","
print(s[:-1])