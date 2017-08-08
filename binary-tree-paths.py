# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        temp = []
        paths = []
        def inorder(node, temp, paths):
            if node:
                temp.append(str(node.val))
                if not node.left and not node.right:
                    paths.append("->".join(temp))
                inorder(node.left, temp, paths)
                inorder(node.right, temp, paths)
                temp.pop()
        inorder(root, temp, paths)
        return paths        
