class CircularQueue():

	def __init__(self, size):  
		self.size = size
		self.queue = [None for j in range(size)]
		self.front = self.cap = -1

	def enqueue(self, data):		
		if ((self.cap	 + 1) % self.size == self.front):
			print(" Queue is Full")			
	
		elif (self.front == -1):
			self.front = 0
			self.cap = 0
			self.queue[self.cap] = data

		else:	
			self.cap = (self.cap + 1) % self.size
			self.queue[self.cap] = data
			
	def dequeue(self):
		if (self.front == -1): 
			print ("Antrian kosong")
			
		elif (self.front == self.cap):
			temp=self.queue[self.front]
			self.front = -1
			self.cap = -1
			return temp

		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
	
		if (self.front == -1):
			print ("Antian Kosong")

		elif (self.cap >= self.front):
			print("Yang ada pada antrian adalah:",end = ' ')
			for j in range(self.front, self.cap + 1):
				print(self.queue[j], end = ' ')
			print ()

		else:
			print ("Yang ada pada antrian circular adalah:",end = ' ')
			for j in range(self.front, self.size):
				print(self.queue[j], end = ' ')
			for j in range(0, self.cap + 1):
				print(self.queue[j], end = ' ')
			print ()

		if ((self.cap + 1) % self.size == self.front):
			print("Antrian penuh")

circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print ("Data yang dihapus adalah = ", circularQueue.dequeue())
print ("Data yang dihapus adalah = ", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()