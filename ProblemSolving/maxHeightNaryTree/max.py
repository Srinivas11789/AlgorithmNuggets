"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        # Recursive Method of finding depth
        def depth(node):
            
            # when a null node is reached from being recursive
            if not node:
                return 0
            else:
                # Node is not None and Node has children (Children check)
                # -- Go with maximum depth child as we progress
                if node.children:
                    return 1 + max([depth(child) for child in node.children])
                else:
                    # When the node has no children count its position
                    return 1
        
        # Root Node Null check
        if not root:
            return 0
        
        return depth(root)
