# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        lis = []
        def inorder(node, lis):
            if node:
                inorder(node.left, lis)
                lis.append(node.val)
                inorder(node.right, lis)
        t = root
        inorder(t, lis)
        s = 0
        e = len(lis) - 1
        while s < e:
            ss = lis[s] + lis[e]
            if ss == k:
                return True
            elif ss > k :
                e -= 1
            else:
                s += 1
        return False
            