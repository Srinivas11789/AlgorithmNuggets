# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        """
        result = head
        if not head:
            return []
        prev = None
        while head and head.next:
                prev = head
                if head.next.next and head.next.val == val:
                    head.next = head.next.next
                head = head.next
                #else:
                #    if head.val == val:
                #        result = head.next
                #    head = head.next
        if head.next == None:
                    if head.val == val:
                        if prev:
                            prev.next = None
                        else:
                            return []
                    return result
        """
        
        # Dont overcomplicate the logic. Iterate through each head and check the value
    
        # Nonetype as input 
        if not head:
            return []
        
        # Setting the initial point to be first non match to val and eliminating everything else
        while head.next and head.val == val:
            head = head.next
        
        # Holders for previous and the result pointer
        result = head
        prev = head
        
        # Eliminating all matches in between
        while head.next:
            head = head.next
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
                
        # Return results
        if result.val == val:
            return []
        else:
            return result
