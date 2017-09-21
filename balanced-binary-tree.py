# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root:
			l = self.maxDepth(root.left)
			if l == -1: return -1
			r = self.maxDepth(root.right)
			if r == -1: return -1
			return -1 if abs(l-r) > 1 else max(l, r) + 1
		return 0

	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.maxDepth(root) != -1
