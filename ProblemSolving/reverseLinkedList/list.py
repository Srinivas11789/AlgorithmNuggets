# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Using an extra list
        if head:
            result = ListNode(head.val)
            result.next = None
            head = head.next
        else:
            return []
        while head:
            temp = ListNode(head.val)
            temp.next = result
            result = temp
            head = head.next
            
        return result

        # Without using an extra list
        
            
            
