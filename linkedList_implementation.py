class Node:
	def __init__(self, value=0, next='EOF'):
		self.value = value
		self.next = next

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.first_node = ''


	def getLastNode(self):
		this_node = self.first_node
		while( not this_node.getNext()=='EOF' ):
			this_node = this_node.getNext()
		return this_node

	def insert(self, value):
		if not self.first_node=='':
			new_node = Node(value)
			last_node = self.getLastNode()
			last_node.setNext(new_node)
		else:
			new_node = Node(value)
			self.first_node = new_node

	def findFirstNodeWithGivenValue(self, value):
		prev = ''
		curr = self.first_node
		while( not curr=='EOF' ):
			if curr.getValue()==value:
				return curr, prev
			else:
				prev = curr
				curr = curr.getNext()
		return -1, -1


	def deleteByValue(self, value):
		this_node, prev = self.findFirstNodeWithGivenValue(value)
		if prev==-1:
			print('Element not found!')
		elif prev=='':
			self.first_node = this_node.getNext() 
		else:
			prev.setNext(this_node.getNext())

	def findNodeAtPosition(self, position):
		prev = ''
		curr = self.first_node
		pos = 1
		while( not curr=='EOF' ):
			if pos==position:
				return curr, prev
			else:
				pos += 1
				prev = curr
				curr = curr.getNext()
		return -1, -1


	def getLength(self):
		count = 0
		this_node = self.first_node
		while( not this_node=='EOF' ):
			this_node = this_node.getNext()
			count+=1
		return count


	def deleteByPosition(self, position):
		length = self.getLength()
		if position>length:
			print('Given position larger than length!')
		else:
			this_node, prev = self.findNodeAtPosition(position)
			if prev==-1:
				print('Element not found!')
			elif prev=='':
				self.first_node = this_node.getNext() 
			else:
				prev.setNext(this_node.getNext())

	def printAllElements(self):
		this_node = self.first_node
		while( not this_node=='EOF' ):
			print(this_node.getValue())
			this_node = this_node.getNext()

	def searchByValue(self, value):
		curr = self.first_node
		position = 1
		while( not curr=='EOF' ):
			if curr.getValue()==value:
				print('Element at position: (counting starts at 1) ', position)
				return position
			else:
				position += 1
				curr = curr.getNext()
		print('Element not found!')

	def searchByPosition(self, position):
		curr = self.first_node
		pos = 1
		while( not curr=='EOF' ):
			if pos==position:
				return curr.getValue()
			else:
				pos += 1
				curr = curr.getNext()
		print('Element not found!')

	def changeValueOfNthElement(self, n, value):
		nth_element, prev = self.findNodeAtPosition(n)
		if prev==-1:
			print('Element not found!')
		else:
			nth_element.setValue(value)

class Queue:
	def __init__(self):
		self.ll = LinkedList()

	def enqueue(self, val):
		self.ll.insert(val)

	def dequeue(self):
		val = self.ll.searchByPosition(1)
		self.ll.deleteByPosition(1)
		return val

	def printAllElements(self):
		self.ll.printAllElements()

if __name__ == '__main__':
	q = Queue()
	q.enqueue(12)
	q.enqueue(2)
	q.enqueue(1)
	q.enqueue(32)
	q.enqueue(14)
	q.enqueue(-10)
	q.dequeue()
	q.dequeue()
	q.dequeue()
	print(q.printAllElements())



