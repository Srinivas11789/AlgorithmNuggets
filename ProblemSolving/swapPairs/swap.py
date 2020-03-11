# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head, parent=None, first_node=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Return Condition
        if not head:
            return first_node
        current = head
        nxt = current.next
        if not nxt:
            if first_node:
                return first_node
            return head
        
        # Perform the necessary operation
        if parent != None:
            parent.next = nxt
        current.next = nxt.next
        nxt.next = current
        
        # Set the initial condition for return
        if first_node == None:
            first_node = nxt
        
        # Break to SubProblems ( each pair ) and call recursive
        return self.swapPairs(current.next, current, first_node)
