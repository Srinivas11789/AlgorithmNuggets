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

