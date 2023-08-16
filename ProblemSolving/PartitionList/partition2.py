# ref: simple 2 pointer approach at https://leetcode.com/problems/partition-list/editorial/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        before = ListNode(0)
        after = ListNode(0)
        rec_after = after
        rec_before = before

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        
        after.next = None
        before.next = rec_after.next
        return rec_before.next

