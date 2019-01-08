"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        # Iterative method of preorder traversal - 100 pass - 176ms
        
        # Stack to keep track of traversal
        self.traverse_stack = [root]
        
        # Result
        self.preorder = []
        
        # Traverse until self.traverse_stack is empty
        while self.traverse_stack:
                # PreOrder - get the first node leftmost 
                current = self.traverse_stack.pop(0)
                if current:
                    # Add to results
                    self.preorder.append(current.val)
                    # add children to the front of the array ==> preOrder
                    if current.children:
                        self.traverse_stack = current.children + self.traverse_stack
        return self.preorder
        
        # Recursive Method ==> 100% pass - 180ms
        """
        # Global list to hold the preorder nodes
        self.preorder = []
        
        # Recursive function
        def traverse(node):
            
            # Node null check
            if not node:
                return
            
            # Append current node to list
            self.preorder.append(node.val)

            # if node contains children, recurse all the children (left -> right)
            if node.children:
                for child in node.children:
                    traverse(child)
        
        # function call
        traverse(root)
    
        return self.preorder
        """
        

        
    
    
        
