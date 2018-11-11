movie = ["国产：无双","国产：影","欧美：蚁人2","欧美：精灵旅社3","欧美：雪怪大冒险","国产：西红市首富"]
"""
def test_filter(array):
	temp = []
	for item in movie:
		if (item.startswith("国产")):
			temp.append(item)
	return temp
"""
"""
def test_filter(func, array):
	#创建一个新列表，用来返回
	temp = []
	#遍历循环参数列表，根据func的规则对列表数据进行过滤，符合条件的放入temp中
	for item in array:
		if(func(item)):
			#将符合过滤条件的元素放入新列表中
			temp.append(item)
	return temp
"""
v = filter(lambda x:x.startswith("国产"),movie)
print(list(v))