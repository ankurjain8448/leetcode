# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def add_carry_only(self, carry, list_, new_list):
		while list_:
			temp = carry + list_.val
			carry = 1 if temp > 9 else 0
			if new_list:
				new_list.next = ListNode(temp%10)
				new_list = new_list.next
			else:
				new_list = ListNode(temp%10)
				self.head = new_list
			list_ = list_.next
		if carry:
			new_list.next = ListNode(carry)

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		new_list = None
		carry = 0
		self.head = None
		ptr_l1 = None
		while l1 and l2:
			temp = carry + l1.val + l2.val
			carry = 1 if temp > 9 else 0
			if new_list:
				new_list.next = ListNode(temp%10)
				new_list = new_list.next
			else:
				new_list = ListNode(temp%10)
				self.head = new_list
			l1 = l1.next
			l2 = l2.next

		self.add_carry_only(carry, l1 if l1 else l2, new_list)
		return self.head
