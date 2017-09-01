# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def swapPairs(self, current):
		"""
		:type current: ListNode
		:rtype: ListNode
		"""
		'''
			0->1->2->3->4
			0->2->1->3->4
			0->2->1->4->3
		'''
		if not current or not current.next: return current
		dummtHead = ListNode(0)
		dummtHead.next = current
		p = current
		prev = dummtHead
		while p and p.next:
			q = p.next
			r = q.next
			prev.next = q
			q.next = p
			p.next = r
			prev = p
			p = r
		return dummtHead.next
			