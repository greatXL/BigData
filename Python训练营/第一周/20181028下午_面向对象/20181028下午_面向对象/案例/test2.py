class Person:
	def __init__(self, name):
		self.name = name

	def run(self):
		print("跑")

p1 = Person("LiLei")
p2 = Person("HanMeimei")
p2 = p1
p2.name = "Sheldon"
print(p1.name)
print(p2.name)