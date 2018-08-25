class Queue:
	def __init__(self):
		self.values = []

	def enqueue(self, val):
		self.values.append(val)

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

	def reverse(self):
		if not self.isEmpty():
			x = self.dequeue()
			self.reverse()
			self.enqueue(x)


if __name__ == '__main__':
	q = Queue()
	q.enqueue(12)
	q.enqueue(2)
	q.enqueue(1)
	q.enqueue(32)
	q.enqueue(14)
	q.enqueue(-10)
	print(q.values)
	q.reverse()
	print('reverse: ', q.values)

