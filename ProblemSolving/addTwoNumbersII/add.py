# 100 pass
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Brute Force
        one = []
        while l1:
            one.append(str(l1.val))
            l1 = l1.next
        
        two = []
        while l2:
            two.append(str(l2.val))
            l2 = l2.next     
            
        sumi = list(str(int("".join(one))+int("".join(two))))
        
        result = ListNode(sumi[0])
        ans = result
        sumi.pop(0)
        print sumi
        while sumi:
            node = ListNode(sumi[0])
            result.next = node
            result = result.next
            sumi.pop(0)
        
        return ans
            
