class Person:
	def __init__(self, name):
		self.name = name

	def run(self):
		print("跑")

def fun(per):
	per.name = "Sheldon"
	print(per.name)
p1 = Person("LiLei")
fun(p1)
print(p1.name)

