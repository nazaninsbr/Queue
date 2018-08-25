class Dequeue:
	def __init__(self):
		self.values = []

	def isEmpty(self):
		if len(self.values)==0:
			return True
		return False 

	def addToFront(self, x):
		self.values = [x] + self.values

	def removeFromFront(self):
		if not self.isEmpty():
			val = self.values[0]
			del self.values[0]
			return val
		return -1

	def addToRear(self, x):
		self.values.append(x)

	def removeFromRear(self):
		if not self.isEmpty():
			val = self.values[-1]
			del self.values[-1]
			return val
		return -1

if __name__ == '__main__':
	dq = Dequeue()
	dq.addToRear(12)
	dq.addToRear(22)
	dq.addToRear(32)
	dq.addToFront(42)
	print(dq.values)
	print(dq.removeFromRear())
	print(dq.removeFromFront())
	print(dq.values)