# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def insert(self, val):
		node = ListNode(val)
		if self.head is None :
			self.list_ = node
			self.head = self.list_
		else:
			self.list_.next = node
			self.list_ = self.list_.next
		

	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		self.list_ = None
		self.head = None
		while l1 and l2:
			if l1.val < l2.val:
				self.insert(l1.val)
				l1 = l1.next
			else:
				self.insert(l2.val)
				l2 = l2.next

		while l1:
			self.insert(l1.val)
			l1 = l1.next

		while l2:
			self.insert(l2.val)
			l2 = l2.next
		return self.head
