"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        # Logic 1: 40ms 100% faster 
        # * At every node, we store the longest height of its children
        # * We can add up between children to obtain the max length through this subtree root node or return the max length of its children including itself
        
        # global diameter
        self.diameter = 0
        
        def find_diameter(node):
            
            # Null Check
            if not node:
                return 
            
            # [Recursion] Obtain height of all children by traversing
            heights = [] 
            for n in node.children:
                heights.append(find_diameter(n))
            
            # At current subtree root node... 
            heights.sort()
            
            # Max height of a child if children exists else 0
            current_max = heights[-1] if heights else 0
                
            # Check if max diameter passes through this node ( Ex 1: 5-3-[1]-2 )
            if len(heights) > 1 and heights[-1] + heights[-2] > self.diameter:
                self.diameter = heights[-1] + heights[-2]
            
            # Check if max height of child is the diameter ( Ex: [1]-2-3 )
            if current_max > self.diameter:
                self.diameter = current_max
                
            # Return the max height of child including the current subtree root node ( adding itself ) for recursion to continue...
            return 1 + current_max
        
        find_diameter(root)
        return self.diameter
            
            
