"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """  
        
        """
        # Recursive Solution
        def order(self, root):   
            if root:
                if root.children:
                    for child in root.children:
                        order(self, child)
                self.result.append(root.val)
    
        self.result = []
        order(self, root)
        return self.result
        """
        
        # Iterative Solution??
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            current = stack.pop()
            result.append(current.val)
            stack.extend(current.children)
        return result[::-1]
