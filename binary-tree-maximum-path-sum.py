# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	# https://leetcode.com/problems/binary-tree-maximum-path-sum/description
	def postorder(self, node):
		if node:
			l = self.postorder(node.left)
			r = self.postorder(node.right)
			self.max_sum = max(self.max_sum, l+r+node.val)
			return_val = max(l ,r) + node.val
			return return_val if return_val > 0 else 0
		return 0

	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		self.max_sum = root.val
		self.postorder(root)
		return self.max_sum
