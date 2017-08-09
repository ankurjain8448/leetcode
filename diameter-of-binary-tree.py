# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		max_ans = [0]
		def iteration(node):
			if node:
				l = iteration(node.left) + 1
				r = iteration(node.right) + 1
				max_ans[0] = max(max_ans[0] , l+r)
				return max(l, r)
			else:
				return -1

		iteration(root)
		return max_ans[0]
