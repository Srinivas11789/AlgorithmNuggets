# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
        # 100 pass
        # - Evaluated most with some help from reference to finish off
        # - https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC%2B%2BPython-Next-Greater-Element
        # Stack to keep track of nodes that are of lesser value ( next greater yet to be found)
        stack = []
        # Result to hold nodes whose next greater has been found
        result = []
        # traverse length of the list as we traverse
        count = 0
        
        # Traverse List
        while head:
            # Next greater is found
            while stack and head.val > stack[-1][1]:
                result[stack.pop()[0]] = head.val
            # Append to stack the index of occurrence and value whose next greater should be found
            stack.append([count, head.val])
            # Next greater will eventually be found, else 0 so add 0 by default
            result.append(0)
            count += 1
            head = head.next
        return result
    
                    
            """
            print stack, result, count
            if stack and head.val < stack[-1]:
                stack.append(head.val)
            else:
                while stack and head.val > stack[0]:
                    stack.pop(0)
                    result.append(head.val)
                stack.append(head.val)
            if not stack:
                #    if count == len(result):
                #        result.append(0)
                #if result[-1] == head.val:
                #    result.append(0)
                #else:
                stack.append(head.val)
            head = head.next
            count += 1
            """
