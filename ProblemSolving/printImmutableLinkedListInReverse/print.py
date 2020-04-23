#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
		
        # Logic 1: Naive iteration logic --> Solving with Space ( Improve to const space complexity ) - 100 pass 52% faster but we are using O(N) SPACE Complexity
        # * usually we can make -> to <- for reversing a list but we want to do this in immutable fashion
        """
        visited = []
        next_node = head
        while next_node:
            visited.append(next_node)
            next_node = next_node.getNext()
        while visited:
            visited.pop().printValue()
        """ 
        
        # Logic 2: Follow up to use constant space and linear time complexity - 25% faster - 100 pass
        # RECURSIVE/Divide&Conquer APPROACH
        # ref: https://leetcode.com/problems/print-immutable-linked-list-in-reverse/discuss/445408/Python-4-solutions-space-complexity-O(n)-O(n(1t))-O(lgn)-O(1)
        def length_of_list(node):
            length = 0
            while node:
                length += 1
                node = node.getNext()
            return length
    
        def print_in_reverse(node, n):
            if n > 1:
                mid = node
                for i in range(n//2):
                    mid = mid.getNext()
                print_in_reverse(mid, n-n//2)
                print_in_reverse(node, n//2)
            elif n > 0: # Remaining node that is the last in subset
                node.printValue()                
        
        n = length_of_list(head)
        print_in_reverse(head, n)
        
        
        # Thoughts
        # * slow/fast pointer logic
        # * n*O(N) iterations? 
        # * o(n//2) space?
