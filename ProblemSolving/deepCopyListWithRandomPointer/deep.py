"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        # Logic 1: 69.36% faster
        
        # Variable declaration
        copy = None
        nodes = {}
        prev = None
        result = None
        ref = head
        
        # O(1) iteration for current node and next
        while head:
            nodes[head] = Node(head.val, None, None)
            if not result:
                result = nodes[head]
            if prev:
                nodes[prev].next = nodes[head]
            prev = head
            head = head.next
        
        # Another O(1) iteration to decide the random
        while ref:
            if ref.random:
                nodes[ref].random = nodes[ref.random]
            else:
                nodes[ref].random = None
            ref = ref.next
        return result
                
        
