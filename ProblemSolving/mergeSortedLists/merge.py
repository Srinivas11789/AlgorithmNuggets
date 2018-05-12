# Try doing the same in o(1) space combined within list 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

	# Using an extra new list declared

        if not l1 and not l2:
            return []
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            result = ListNode(l1.val)
            l1 = l1.next
        else:
            result = ListNode(l2.val)
            l2 = l2.next
        
        ans = result
        
        while l1 and l2:
            if l1.val < l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next
        
        if l1 and l2: 
            if l1.val < l2.val:
                result.next = ListNode(l1.val)
                result = result.next
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                result = result.next
                l2 = l2.next
        
        while l1 and l1.next:
            result.next = ListNode(l1.val)
            result = result.next
            l1 = l1.next

        while l2 and l2.next:
            result.next = ListNode(l2.val)
            result = result.next
            l2 = l2.next
        
        if l1:
            result.next = ListNode(l1.val)
            result = result.next
        
        if l2:
            result.next = ListNode(l2.val)
            result = result.next
        
        return ans
        
