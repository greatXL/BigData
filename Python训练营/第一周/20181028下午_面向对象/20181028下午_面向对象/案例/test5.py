"""
类: SweetPotato

属性：
cookedLevel：0-3生的3-5半生不熟5-8正好>8烤焦了
cookedString:当前地瓜的生熟程度
condiments:列表

方法：
cook(self, time):
addCondiment(self,condiment)
__init__(self):
__str__():生的(蛋黄酱，芥末酱)
"""
class SweetPotato:

	def __init__(self):
		self.cookedLevel = 0
		self.cookedString = "生的"
		self.condiments = []

	def cook(self, time):
		self.cookedLevel += time
		if(self.cookedLevel>8):
			self.cookedString = "烤焦了"
		elif (self.cookedLevel>5):
			self.cookedString = "正好"
		elif (self.cookedLevel>3):
			self.cookedString = "半生不熟"
		else:
			self.cookedString = "生的"


	def addCondiments(self, condiment):
			self.condiments.append(condiment)

	def __str__(self):
		msg = self.cookedString
		if (len(self.condiments)>0):
			msg += "("
			for item in self.condiments:
				msg = msg + item + ","
			msg = msg.strip(",")
			msg += ")"
		return msg

sp = SweetPotato()
sp.cook(9)
sp.addCondiments("香辣酱")
sp.addCondiments("芥末酱")
sp.addCondiments("番茄酱")
print(sp)