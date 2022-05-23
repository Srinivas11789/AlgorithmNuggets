# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 2 iteration mode 2*O(n) = O(n)
        
        # 1. find length of list
        l = head
        length = 1
        while l:
            length += 1
            l = l.next
            
        # 2. find nth node to replace
        i = head
        ind = 1
        left = None
        while i:
            pos = length-ind
            if pos == n:
                if not left:
                    head = i.next
                elif left and i.next:
                    left.next = i.next
                else:
                    left.next = None
            ind += 1
            left = i
            i = i.next
        
        return head
