# Definition for a binary tree node.
# class TreeNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution(object):
	root = None
	
	def insert(self, x, current_node):
		node = TreeNode(x)
		if not self.root:
			self.root = node
			current_node = self.root
			return current_node
		# root_node = self.root
		root_node = current_node

		while root_node:
			if x < root_node.val:
				if root_node.left :
					root_node = root_node.left
				else:
					root_node.left = node
					current_node = root_node.left 
					break
			if x > root_node.val:
				if root_node.right:
					root_node = root_node.right
				else:
					root_node.right = node
					current_node = root_node.right
					break
		return current_node

	def binary_traverse(self, a, start, end, cur_node):
		if start <= end:
			mid = (start+end)/2
			cur_node = self.insert(a[mid], cur_node)
			self.binary_traverse(a, start, mid-1, cur_node)
			self.binary_traverse(a, mid+1, end, cur_node)


	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		self.binary_traverse(nums, 0, len(nums)-1, None)
		return self.root
