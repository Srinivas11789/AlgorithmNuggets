# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # Logic 1: Store values as less and more, perform 2*(O(N)) list iteration
        
        """
        less = [] # 1,2,2 1->2->2
        more = [] # 4,3,5 4->3->5
        
        second = head
        result = head
        
        while head:
            if head.val < x:
                less.append(head.val)
            else:
                more.append(head.val)
            head = head.next
            
        print(less, more)
            
        while second:
            if less:
                second.val = less.pop(0)
            elif more:
                second.val = more.pop(0)
            second = second.next
            
        return result
        """
        
        # Logic 2: Create sublists for less and more with O(N) iteration and merge
        
        less = None
        more = None
        lhead = None
        mhead = None
        
        while head:
            if head.val < x:
                if not less:
                    lhead = head
                    less = head
                else:
                    less.next = head
                    less = less.next
            else:
                if not more:
                    more = head
                    mhead = head
                else:
                    more.next = head
                    more = more.next
            
            head = head.next
            
        #print(lhead.val, mhead.val, more.val, less.val)
        if less:
            less.next = mhead
        if more:
            more.next = None
        if not lhead:
            lhead = mhead
            
        return lhead
            
