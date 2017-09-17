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
		maps = {}
		temp = head
		new_List_head = None
		index = 0
		map_node_index = {}
		map_new_node_index = {}
		map_random_pointer = {}
		if head:
			new_List_head = RandomListNode(temp.label)
			new_List = new_List_head
			map_node_index[temp] = index
			map_new_node_index[index] = new_List
			temp = temp.next
			index += 1
		while temp:
			new_List.next = RandomListNode(temp.label)
			new_List = new_List.next
			map_node_index[temp] = index
			map_new_node_index[index] = new_List
			temp = temp.next
			index += 1
		
		temp = head
		new_List_head_ptr = new_List_head
		while temp:
			new_List_head_ptr.random = map_new_node_index[map_node_index[temp.random]]
			temp = temp.next
			new_List_head_ptr = new_List_head_ptr.next

		return new_List_head
