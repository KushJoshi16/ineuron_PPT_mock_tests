
class Queue:
	def __init__(self):
		self.head = list()
		self.size = 0

	def __str__(self):
		cur = 0
		out = ""
		for cur in range(self.size):
			out += str(self.head[cur]) + "->"
			cur += 1
		return out[:-2]

	def isEmpty(self):
		return self.size == 0

	def enqueue(self, value):
		self.head.append(value)
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			raise Exception("Dequeue from an empty queue")
		remove = self.head[0]
		self.head.pop(0)
		self.size -= 1
		return remove


if __name__ == "__main__":
	queue = Queue()
	for i in range(1, 11):
		queue.enqueue(i)
	print(f"queue: {queue}")

	for _ in range(1, 6):
		remove = queue.dequeue()
		print(f"Pop: {remove}")
	print(f"queue: {queue}")
