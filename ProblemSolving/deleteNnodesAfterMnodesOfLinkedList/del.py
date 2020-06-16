# Logic 1: follow the prob steps, at every start node, skip some and delete others, jump to a new start and then start the loop again - 100 pass - 78% faster

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        # Store head ref to return
        result = head
        # Iterate until end
        while head:
            # Refresh n, m at every start node
            noDel = m-1
            delete = n
            # no delete m
            while head and noDel:
                head = head.next
                noDel -= 1
            # delete n
            while head and head.next and delete:
                head.next = head.next.next
                delete -= 1
            # move to a new start
            if head:
                head = head.next
        return result
