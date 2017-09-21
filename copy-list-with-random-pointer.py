# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#	 def __init__(self, x):
#		 self.label = x
#		 self.next = None
#		 self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		temp = head
		dummyHead = RandomListNode(00)
		new_list = dummyHead
		mappings = {}
		while temp:
			new_list.next = RandomListNode(temp.label)
			mappings[temp] = new_list.next
			new_list = new_list.next
			temp = temp.next

		old_list = head
		new_list = dummyHead.next
		while old_list is not None:
			if old_list.random:
				new_list.random = mappings[old_list.random]
			old_list = old_list.next
			new_list = new_list.next

		return dummyHead.next
