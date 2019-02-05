class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        nodes = []
        
        # Linked list traversal
        while root:
            nodes.append(root.val)
            root = root.next
        
        n = len(nodes)
        
        result = []
        
        if n == 0:
            return [[]*(k)]
        
        # Equal parts
        if n%k == 0:
            divide = n//k
            while nodes:
                result.append(nodes[:divide])
                nodes = nodes[divide:]
        else:
            if n < k:
                divide = 1
                while nodes:
                    result.append(nodes[:divide])
                    nodes = nodes[divide:]
                while len(result) < k:
                    result.append([])
            else:
                divide = k
                while len(nodes) > divide:
                    result = nodes[-divide:] + result
                    nodes = nodes[:divide]
                result = nodes + result
                    
        return result
