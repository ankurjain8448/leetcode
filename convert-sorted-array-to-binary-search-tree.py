# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	root = None
	
	def insert(self, x):
		# print "inserting : ", x
		node = TreeNode(x)
		if not self.root:
			self.root = node
			return
		root_node = self.root
		while root_node:
			if x < root_node.val:
				if root_node.left :
					root_node = root_node.left
				else:
					root_node.left = node
					break
			if x > root_node.val:
				if root_node.right:
					root_node = root_node.right
				else:
					root_node.right = node
					break
		return

	def binary_traverse(self, a, start, end):
		if start <= end:
			mid = (start+end)/2
			self.insert(a[mid])
			self.binary_traverse(a, start, mid-1)
			self.binary_traverse(a, mid+1, end)

	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		self.binary_traverse(nums, 0, len(nums)-1)
		# print self.root.val
		self.preorder(self.root)
		return self.root

	def preorder(self, node):
		if node:
			print node.val
			self.preorder(node.left)
			self.preorder(node.right)

arr = [1,2,3,4,5]
obj = Solution()
root = obj.sortedArrayToBST(arr)