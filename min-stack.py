class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.current_index = -1
		self.stack = []
		self.minstack = []


	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.stack.append(x)
		self.current_index += 1
		if self.current_index == 0:
			self.minstack.append(x)
			return None
		if x > self.minstack[-1]:
			self.minstack.append(self.minstack[-1])
		else:
			self.minstack.append(x)
		return None


	def pop(self):
		"""
		:rtype: void
		"""
		if self.current_index > -1:
			self.minstack.pop()
			self.stack.pop()
			self.current_index -= 1
		return None
		

	def top(self):
		"""
		:rtype: int
		"""
		return self.stack[-1]
		

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.minstack[-1]
		


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()