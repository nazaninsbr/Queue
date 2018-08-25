class Queue:
	def __init__(self):
		self.values = []
		self.front = -1
		self.rear = -1

	def enqueue(self, val):
		if self.front==-1:
			self.front = val
		self.values.append(val)
		self.rear = val


	def isEmpty(self):
		if len(self.values)==0:
			return True
		return False


	def dequeue(self):
		if not self.isEmpty():
			val = self.values[0]
			del self.values[0]
			if not self.isEmpty():
				self.front = self.values[0]
			else:
				self.front = -1 
			return val
		else:
			return -1

	def Front(self):
		return self.front

	def Rear(self):
		return self.rear

if __name__ == '__main__':
	q = Queue()
	q.enqueue(12)
	q.enqueue(2)
	q.enqueue(1)
	q.enqueue(32)
	q.enqueue(14)
	q.enqueue(-10)
	print('front: ',q.Front())
	print('rear: ',q.Rear())
	q.dequeue()
	q.dequeue()
	q.dequeue()
	print('front: ',q.Front())
	print('rear: ',q.Rear())


