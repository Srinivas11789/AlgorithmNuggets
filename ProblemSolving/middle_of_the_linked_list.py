# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        # using O(N) space complexity => 100 pass
        # list to store all the node values
        nodes = []  
        # Iterating the linkedin list until null
        while head:
            nodes.append(head.val)
            head = head.next
        # return all the nodes from the middle of the list 
        return nodes[len(nodes)//2:]
        """
        
        # 2 pointer method - mid and the last
        # using O(1) space and O(N) route => 100 pass
        
        # Mid element
        mid_pointer = head
        # Mid length
        mid_length = 1
        # Last element 
        last_pointer = head.next
        # length until the current elemenet
        curr_length = 2
        # iterating the last element one by one
        while last_pointer:
            last_pointer = last_pointer.next
            curr_length += 1
            # iterating mid element until the mid from the last element
            while mid_length < curr_length//2:
                mid_length += 1
                mid_pointer = mid_pointer.next
        print mid_pointer.val, mid_length, last_pointer, curr_length
        
        # Result list generation
        result = []
        # if even length, take the second highest element
        if curr_length%2 != 0:
            mid_pointer = mid_pointer.next
        while mid_pointer:
            result.append(mid_pointer.val)
            mid_pointer = mid_pointer.next
        return result
            
