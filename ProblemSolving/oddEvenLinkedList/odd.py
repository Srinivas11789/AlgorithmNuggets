# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Empty handle
        if not head:
            return []
        
        # Result - store result node as head (to return output as we change head while we move)
        result = head
        
        # Current odd node visited (Used to append next odd node) 
        odd_node = head
        
        if not head.next:
            return head
        
        # Current even node visited (Used to find the next odd node to move) 
        even_node = head.next
        
        
        # Iterate until the even node's next (odd node) doesnt exist
        while even_node.next:
            # Insert odd node after last odd_node visited
            last_even_node = odd_node.next
            odd_node.next = even_node.next
            even_node.next = even_node.next.next
            # Move as we make the changes
            odd_node = odd_node.next
            odd_node.next = last_even_node
            #print even_node.val, odd_node.val
            if even_node.next:
                even_node = even_node.next
        return head
        
        
        
