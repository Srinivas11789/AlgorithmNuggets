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
    
        # Init variables
        front = head
        parent = None
        duplicate = None

        while head and head.next:
            if parent:
                print(parent.val, head.val, head.next.val)
            
            # Find Duplicates
            while head and head.next and head.val == head.next.val:
                if not duplicate:
                    duplicate = head
                head = head.next
            
            # Strip duplicate nodes
            if duplicate and head.val == duplicate.val:
                if parent:
                    parent.next = head.next
                    head = head.next
                else:
                    temp = head
                    head = head.next
                    front = head
                    temp.next = None
                duplicate = False
            else:     
                # Next Iteration Vars
                parent = head
                head = head.next

        return front
