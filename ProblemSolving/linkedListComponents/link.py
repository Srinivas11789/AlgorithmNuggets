# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# lt medium - 100 pass
# Remove or Delete Method - remove or delete from G as we move through the linked list and count
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        count = 0
        # Logic to iterate over the linked list
        while head:
            # Logic to check for the connected components
            """
            # Complex and not correct
            if head.val in G and head.next and head.next.val in G and G.index(head.val) < G.index(head.val):
                count += 1
            """
            if head.val in G:
                G.remove(head.val)
                while head.next and head.next.val in G:
                    G.remove(head.next.val)
                    head = head.next
                count += 1
            head = head.next
        return count
        
