# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
class Solution(object):

	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		ans = []
		for each_list in lists:
			if each_list:
				head = each_list
				while head:
					ans.append(head.val)
					head = head.next
		if ans:
			ans.sort()
			head = ListNode(ans[0])
			temp = head
			for i in ans[1:]:
				temp.next = ListNode(i)
				temp = temp.next
			ans = head
		return ans


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):

# 	def get_min_node(self, lists):
# 		import sys
# 		ans = sys.maxint
# 		current_index = -1
# 		for index, each_list in enumerate(lists):
# 			if each_list and each_list.val < ans:
# 				ans = each_list.val
# 				current_index = index
# 		if current_index == -1:
# 			return None
# 		temp = ans
# 		lists[current_index] = lists[current_index].next
# 		return temp

# 	def mergeKLists(self, lists):
# 		"""
# 		:type lists: List[ListNode]
# 		:rtype: ListNode
# 		"""
# 		head = self.get_min_node(lists)
# 		if head is None:
# 			return []
# 		head = ListNode(head)
# 		temp = head
# 		while True:
# 			node = self.get_min_node(lists)
# 			if node is None:
# 				break
# 			else:
# 				temp.next = ListNode(node)
# 				temp = temp.next
# 		return head
