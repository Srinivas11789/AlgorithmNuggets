# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        first = head # first half of string
        other = head.next # Other half of string
        first.next = None
        
        while first and other:
            if other.next and first.val == other.next.val:
                other = other.next
                break
            elif first.val == other.val:
                break

            temp = first
            first = other
            other = other.next
            first.next = temp
        
        if not first or not other:
            return False
        
        print(first.val, other.val)
        
        while first and other:
            if first.val == other.val:
                pass
            else:
                return False
            first = first.next
            other = other.next
        
        if first or other:
            return False
        
        return True
