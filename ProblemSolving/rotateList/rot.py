# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # 100 pass - Nice logic - Make the list a circular list and perform the operations
        
        # Only head handle
        if not head:
            return head
        if k == 0:
            return head
        if not head.next:
            return head
        
        # Find the last node and make it circular list
        
        # Store the first list element
        first = head
        length = 1
        while first.next != None:
            length += 1
            first = first.next

        # Make k within the range of the list length - to find where to make the break
        k = (length-k)%length

        if k == 0:
            # Break the circularity before returning - the output was iterating through the list, this caused the return to go through a loop as the list was made circular by default while reading the list. Fixing with this logic worked.
            return head
        else:
            # Make it a circular list
            first.next = head
        
        # Goto kth position and break the list from being circular
        i = 1
        first = head
        while i < k:
            i += 1
            first = first.next
        
        head = first.next
        first.next = None
        
        return head
            
        
        
        
        
        
        
