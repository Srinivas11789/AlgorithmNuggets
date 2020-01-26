# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Logic 1: 2*O(N) Iteration over the linked list - 100 pass 39% faster
        # 1. find the length of the linked list
        # 2. delete the node 
        
        front = head
        length = 0
        
        while head:
            length += 1
            head = head.next
        
        head = front
        target = length - n + 1
        current = 0
        prev = None
        
        while head:
            current += 1
            if current == target:
                if prev:
                    prev.next = head.next
                    head = head.next
                elif length == 1:
                    return ListNode("")
                else:
                    prev = head
                    head = head.next
                    prev.next = None
                    front = head
            else:
                prev = head
                head = head.next

        return front
