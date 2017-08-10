class Solution(object):
	def myAtoi(self, string):
		"""
		:type str: str
		:rtype: int
		"""
		n = len(string)
		i = 0
		num = 0
		multiplier = 10
		is_negative = False
		while i < n and string[i] == ' ':
			i += 1
		if i < n :
			if string[i] == '+':
				i += 1
			elif string[i] == '-':
				is_negative = True
				i+=1
			while i < n:
				try:
					p = int(string[i])
					num = num*multiplier + p
					if not is_negative and num > 2147483647 :
						return 2147483647
					if is_negative and num > 2147483648:
						return -2147483648
				except Exception as exp:
					break
				i += 1
			return -num if is_negative else num 
		return 0

obj = Solution()
while True:
	print obj.myAtoi(str(input()))
	pass