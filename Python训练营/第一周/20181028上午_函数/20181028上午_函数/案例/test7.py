#调用一个函数，在函数中传入一个列表，该函数会返回一个新的列表，新列表中每个元素的值是参数列表每个元素的值加10
num = [12,3,2,1,6,67]
"""
def test_map(array):
	temp = []
	for item in array:
		temp.append(item + 10)
	return temp
"""
"""
def test_map(func,array):
	#创建一个新列表，用来返回
	temp = []
	#遍历循环参数列表，item表示参数列表中的每一个元素
	for item in array:
		#根据传入的func对参数列表中的每一个元素进行处理
		v = func(item)
		#将处理后的结果添加到新列表中，最后返回
		temp.append(v)
	return temp
"""
v = map(lambda x:x+10, num)
print(list(v))