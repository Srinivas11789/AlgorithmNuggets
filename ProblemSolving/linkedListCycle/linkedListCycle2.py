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
        
        
            
        
        
