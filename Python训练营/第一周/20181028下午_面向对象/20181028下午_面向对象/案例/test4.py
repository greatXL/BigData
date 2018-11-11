class Car:

	def __init__(self,wheelNum,color):
		self.wheelNum = wheelNum
		self.color = color

	def __str__(self):
		return "我的颜色是：" + self.color + " 我有" + str(self.wheelNum) + "个轮子"	

	def move(self):
		print("动起来了")

c = Car(4, "白色")
print(c)
