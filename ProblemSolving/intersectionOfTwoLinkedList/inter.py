# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Store the head pointers
        a = headA
        b = headB
        
        # Null check and return No intersection when anyone is empty
        if not headA or not headB :
            return None

        # When headA and headB exist and are not equal,keep iterating the loop
        while headA and headB and headA != headB:
            
            # traversing through the next node
            headA = headA.next
            headB = headB.next
            
            # Equality condition of finding the intersection and returning the current pointer 
            if headA == headB:
                return headA
            
            # Inequal length of linked list handling - when one list exhaust start from the beginning of other list hence traverse all the elements which have not been compared iteratively
            if not headA:
                headA = b
            if not headB:
                headB = a

        return headA
        
