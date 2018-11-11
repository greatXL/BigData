#无参数，无返回值
#计算1到100的和并输出
def fun1():
	i = 1
	sum = 0
	while i <= 100:
		sum += i
		i += 1
	print(sum)

#无参数，有返回值
#计算1到100的值，并返回
def fun2():
	i = 1
	sum = 0
	while i <= 100:
		sum += i
		i += 1
	return sum
v = fun2()

#有参数，无返回值
#判断一个年份是否是闰年
def fun3(year):
	if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
		print("该年是闰年")
	else:
		print("不是闰年")

#有参数，有返回值
#判断一个年份是否是闰年，如果是返回True，否则返回False
def fun4(year):
	if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
		return True
	else:
		return False
print(fun4(2001))