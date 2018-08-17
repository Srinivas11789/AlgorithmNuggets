"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        """
        # Iterative
        while not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            result.append([])
            n = len(stack)
            while n > 0:
                current = stack.pop(0)
                result[-1].append(current.val)
                stack.extend(current.children)
                n -= 1
        return result 
        """
        
        # Recursive
        def recurse_level(root, level):
            if level == self.length:
                self.result.append([root.val])
                self.length += 1
            else:
                self.result[level].append(root.val)
                
            if root.children:
                for child in root.children:
                    recurse_level(child, level+1)
        
        self.result = []
        self.length = 0
        
        if not root:
            return []
        
        recurse_level(root, 0)
        return self.result
        
        
        
        
        
        
            
        
                
        
