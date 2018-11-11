class Person:

	def run(self):
		print("今天我要跑十公里")

	def eat(self):
		print("跟着我有肉吃")

	def fight(self):
		print("你瞅啥？")

p = Person()#实例化一个对象
p.eat()
p.fight()
p.name = "张三"
print(p.name)

