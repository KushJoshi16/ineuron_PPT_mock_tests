# Purpose: Stack implementation in Python.
class Stack:
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

	def peek(self):
		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head[self.size - 1]

	def push(self, value):
		self.head.append(value)
		self.size += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head[self.size - 1]
		self.head.pop(self.size - 1)
		self.size -= 1
		return remove


if __name__ == "__main__":
	stack = Stack()
	for i in range(1, 11):
		stack.push(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.pop()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")
