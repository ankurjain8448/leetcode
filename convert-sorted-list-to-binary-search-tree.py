# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def call(self, arr, start, end):
		if start > end:
			return None
		mid = (start+end)/2
		node = TreeNode(arr[mid])
		node.left = self.call(arr, start, mid-1)
		node.right = self.call(arr, mid + 1, end)
		return node

	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		arr = []
		while head:
			arr.append(head.val)
			head = head.next
		return self.call(arr, 0 , len(arr)-1)
