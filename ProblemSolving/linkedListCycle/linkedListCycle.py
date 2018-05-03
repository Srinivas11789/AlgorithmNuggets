"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    # Maintaining an extra list
    """
    visited = []
    while head.next != None:
        if head.next in visited:
            return 1
        visited.append(head.next)
        head = head.next
    return 0
    """
    # Maintaining an extra array
    last = None
    while head.next != None:
        if head.next == head:
            return 1
        last = head
        head = head.next
    return 0


# Alternate solution without using a extra space - floyds power

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Nice hint from discussions - wintop6211
        
        # Floyd's Cycle Detection - Rabbit<hare> and Tortise 
        
        # 2 pointer technique
        tortise = head
        hare = head
        
     
        while hare and hare.next and hare.next.next:
            tortise = tortise.next
            hare = hare.next.next
        
            if hare == tortise:
                return True
        
        return False
        
        
            
        
        

