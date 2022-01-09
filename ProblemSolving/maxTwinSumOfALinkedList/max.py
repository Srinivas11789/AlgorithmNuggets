"""
https://leetcode.com/contest/biweekly-contest-69/problems/maximum-twin-sum-of-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = {}
        index = 0
        
        while head:
            nodes[index] = head.val
            head = head.next
            index += 1
            
        n = len(nodes.keys())
        max_twin_sum = 0
        print(nodes)

        index -= 1
        while index > 0:
            if nodes[index] + nodes[n-index-1] > max_twin_sum:
                max_twin_sum = nodes[index] + nodes[n-index-1]
            index -= 1
        
        return max_twin_sum
