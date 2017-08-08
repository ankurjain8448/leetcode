# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        temp = []
        paths = []
        def inorder(node, temp, paths, s):
            if node:
                temp.append(node.val)
                if not node.left and not node.right and s == node.val:
                    paths.append([i for i in temp])
                inorder(node.left, temp, paths, s - node.val)
                inorder(node.right, temp, paths, s - node.val)
                temp.pop()
        inorder(root, temp, paths, sum)
        return paths
