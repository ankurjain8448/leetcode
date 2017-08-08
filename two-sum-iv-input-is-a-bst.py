# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def basic_approach(self, root, k):
        '''
            time/space : O(n)
        '''
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

    def space_optimized(self, root, k):
        '''
            space : O(logn) , this is recursion depth if tree if tree is balanced
            time : O(n)
        '''
        # some issues while submitting
        ino = self.inorder(root)
        reverse_ino = self.reverse_inorder(root)
        try:
            p1 = ino.next()
            p2 = reverse_ino.next()
            while True:
                ss = p1+p2
                if ss == k:
                    break
                elif ss > k :
                    p2 = reverse_ino.next()
                else:
                    p1 = ino.next()
            return True
        except Exception as exp:
            pass
        return False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.basic_approach(root, k)
        # return self.space_optimized(root, k)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            yield node.data
            self.inorder(node.right)

    def reverse_inorder(self, node):
        if node:
            self.reverse_inorder(node.right)
            yield node.data
            self.reverse_inorder(node.left)      
