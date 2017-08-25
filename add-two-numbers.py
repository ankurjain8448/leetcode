# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		carry = 0
		while l1 and l2:
			temp = carry + l1.val + l2.val
			if temp > 9:
				carry = 1
			else:
				carry = 0
			l1.val = temp % 10
			l1 = l1.next
			l2 = l2.next
			print l1.val
		while l1:
			l1 = l1.next

		while l2:
			l1.next = ListNode(l2.val)
			l1 = l1.next
			l2 = l2.next
		return l1
