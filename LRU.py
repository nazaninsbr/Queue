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

	def length(self):
		return len(self.values)

class Cache:
	def __init__(self, number_of_page_frames):
		self.number_of_page_frames = number_of_page_frames
		self.queue = Queue()

	def acceccPage(self, page_num):
		pages = self.queue.values
		if page_num in pages:
			return "page is in the cashe"
		else:
			if self.queue.length()<self.number_of_page_frames:
				self.queue.enqueue(page_num)
				return "got the page and placed it in the cache"
			else:
				self.queue.dequeue()
				self.queue.enqueue(page_num)
				return "performed LRU policy"

def LRU_cache():
	reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
	number_of_page_frames = 3
	cache = Cache(number_of_page_frames)
	for ref in reference_string:
		print(cache.acceccPage(ref))


if __name__ == '__main__':
	LRU_cache()