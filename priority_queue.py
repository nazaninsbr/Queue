class Queue:
	def __init__(self):
		self.values = []
		self.front = -1
		self.rear = -1

	def enqueue(self, val, priority):
		if self.isEmpty():
			self.values.append([val, priority])
		else:
			added = False
			for itemId in range(len(self.values)):
				if itemId==len(self.values):
					break
				if self.values[itemId][1]<=priority:
					continue
				elif self.values[itemId][1]>priority:
					self.values = self.values[:itemId]+[[val, priority]]+self.values[itemId:]
					added = True
					break
			if added==False:
				self.values.append([val, priority])

	def isEmpty(self):
		if len(self.values)==0:
			return True
		return False


	def dequeue(self):
		if not self.isEmpty():
			val = self.values[0]
			del self.values[0]
			return val
		else:
			return -1

if __name__ == '__main__':
	q = Queue()
	q.enqueue(12, 1)
	q.enqueue(2, 3)
	q.enqueue(1, 2)
	q.enqueue(32, 1)
	q.enqueue(14, 3)
	q.enqueue(-10, 2)
	print(q.values)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	q.enqueue(7, 1)
	print(q.values)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())


