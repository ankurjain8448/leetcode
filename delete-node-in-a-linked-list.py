# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        start = node
        temp = node
        while(node.next):
            temp = node.next
            node.val = temp.val
            if temp.next is None:
                node.next = None