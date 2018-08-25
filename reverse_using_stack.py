class Stack:
	def __init__(self):
		self.values = []

	def push(self, x):
		self.values.append(x)

	def top(self):
		if len(self.values)==0:
			return -1
		return self.values[-1]

	def isEmpty(self):
		return len(self.values)==0

	def pop(self):
		if len(self.values)==0:
			return -1
		x = self.values[-1]
		del self.values[-1]
		return x

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
		tempStack = Stack()

		while not self.isEmpty():
			tempStack.push(self.dequeue())

		while not tempStack.isEmpty():
			self.enqueue(tempStack.pop())

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

