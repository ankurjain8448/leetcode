# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, current):
        """
        :type current: ListNode
        :rtype: ListNode
        """
        '''
			1->2->3->4
			2->1->4->3
        '''
        if not current : return current
        new_head = current
        ptr = None
        while current.next:
        	if ptr is None:
        		ptr = current.next
        		new_head = ptr
        	else:
        		ptr.next = current
        	next = current.next
        	new_current = next.next
        	# swapping
        	next.next = current
        	current.next = new_current
        	current = new_current
        	if not current:
        		break
        return new_head
