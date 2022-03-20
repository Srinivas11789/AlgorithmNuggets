"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def clone(tree1, tree2=None):
            
            if not tree1:
                return
            
            if tree2 == None:
                tree2 = Node(tree1.val)
            
            for child in tree1.children:
                new_child = Node(child.val)
                clone(child, new_child)
                tree2.children.append(new_child)
            
            return tree2
        
        tree2 = clone(root)
        return tree2
        
