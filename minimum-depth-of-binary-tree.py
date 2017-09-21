# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root :
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            if l and r:
                return min(l, r) + 1
            else:
                if l == 0 :
                    return r + 1
                return l + 1
        return 0
