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
		index = 0
		map_node_index = {}
		map_new_node_index = {}

		temp = head

		dummyHead = RandomListNode(00)
		new_list = dummyHead
		while temp:
			new_List.next = RandomListNode(temp.label)
			new_List = new_List.next

			map_new_node_index[index] = new_List
			map_node_index[temp] = index
			temp = temp.next
			index += 1

		old_list = head
		new_list = dummyHead.next
		while old_list is not None:
			if old_list.random:
				new_list.random = map_new_node_index[map_node_index[old_list.random]]
			old_list = old_list.next
			new_list = new_list.next

		return dummyHead.next
