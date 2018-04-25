# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        if not head:
            return result
        if head.next is None:
            return result
        prev = head
        head = head.next
        while head:
            if prev.val == head.val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return result
