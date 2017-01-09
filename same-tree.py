# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # import Queue
        q1 = []
        q1.append(p)
        q2 = []
        q2.append(q)
        flag = True
        if p is None and q is None:
            return flag
        if (p and q is None ) or (q and p is None):
            return False
        while ( len(q1) and len(q2)):
            a = q1.pop(0)
            b = q2.pop(0)
            if a.val != b.val:
                flag = False
                break
            if (a.left and not b.left) or (b.left and not a.left):
                flag = False
                break
            if (a.right and not b.right) or (b.right and not a.right):
                flag = False
                break

            if a.left and b.left :
                q1.append(a.left)
                q2.append(b.left)
                
            if a.right and b.right:
                q1.append(a.right)
                q2.append(b.right)
        return flag
        