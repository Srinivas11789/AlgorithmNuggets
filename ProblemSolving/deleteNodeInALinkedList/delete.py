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
        
        nxt = node
        while nxt:
            if nxt.next:
                nxt.val = nxt.next.val
            if not nxt.next.next:
                nxt.next = None
            nxt = nxt.next
