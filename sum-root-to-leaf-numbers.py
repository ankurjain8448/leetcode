# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_int(arr):
            ans = arr[0]
            counter = 10
            for i in xrange(1, len(arr)):
                ans = ans*counter + arr[i]
            return ans
        temp = []
        ans = [0]
        def inorder(node, ans, temp):
            if node:
                temp.append(node.val)
                if not node.left and not node.right :
                    ans[0] += get_int(temp)
                inorder(node.left, ans, temp)
                inorder(node.right, ans, temp)
                temp.pop()
        inorder(root, ans, temp)
        return ans[0]
