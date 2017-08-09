# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findFrequentTreeSum(self, root):
		global_dict = {} # key "sum" , value : 'freq'
		max_freq = [0]
		def postorder(node, global_dict):
			if node:
				l_sum = postorder(node.left, global_dict)
				r_sum = postorder(node.right, global_dict)
				temp = l_sum + r_sum + node.val
				if temp in global_dict:
					global_dict[temp] += 1
				else:
					global_dict[temp] = 1
				max_freq[0] = max(max_freq[0], global_dict[temp])
				return temp
			else:
				return 0
		postorder(root, global_dict)
		return [ k for k , v in global_dict.iteritems() if v == max_freq[0]]
