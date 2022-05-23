# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        rtnResult = result
        carry = 0
        
        while l1 and l2:
            theSum = l1.val + l2.val + carry
            carry = theSum//10
            result.val = theSum%10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                result.next = ListNode()
                result = result.next
            
        while l1:
            theSum = l1.val + carry
            carry = theSum//10
            result.val = theSum%10
            l1 = l1.next
            if l1:
                result.next = ListNode()
                result = result.next
            
        while l2:
            theSum = l2.val + carry
            carry = theSum//10
            result.val = theSum%10
            l2 = l2.next
            if l2:
                result.next = ListNode()
                result = result.next
                
        if carry:
            result.next = ListNode(carry)
            
        return rtnResult
