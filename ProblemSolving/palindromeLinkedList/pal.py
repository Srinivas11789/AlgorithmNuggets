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
        
        # O(N) runtime + O(1) space
        # A nice logic from discussions - StefanPochmann
        # Reversed first half == second half ==> Palindrome
        
        # reverse of the first half can be obtained by starting from middle element
        reverse = None
        
        # 2 pointers, 
        # slow - to track the comparison
        # fast - to help finding the middle element
        slow = fast = head
        
        # Finding middle element
        while fast and fast.next:
            fast = fast.next.next
            # Reverse pointers to create reverse list
            reverse, reverse.next, slow = slow, reverse, slow.next
        
        # Past the middle element
        if fast:
            slow = slow.next
        
        # Iterating reverse and slow to check for match
        while reverse and reverse.val == slow.val:
            reverse = reverse.next
            slow = slow.next

        if reverse:
            return False
        else:
            return True
            
        
            
        
