"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def levelOrderTraverseIterative(self, node):
        
        # 0. null check
        if not node:
            return
        
        # 1. iterative level order traverse
        stack = [node]
        
        # full iteration
        while stack:
            
            # per level setting and iteration
            n = len(stack)
            nxt_lvl = []
            
            # per level iteration
            while n:
                current = stack.pop(0)
                
                # next logic
                if stack:
                    current.next = stack[0]
                else:
                    current.next = None
                    
                # iterative traversal
                if current.left:
                    nxt_lvl.append(current.left)
                if current.right:
                    nxt_lvl.append(current.right)
                    
                n -= 1
            
            # new level continue
            stack = nxt_lvl
            
        return
        
        
    def levelOrderTraverseRecursive(self, node, level):
        
        # 0. record node by level
        if level not in self.levels:
            self.levels[level] = []
            
        # 1. check for existing left nodes and add right node
        if self.levels[level]:
            self.levels[level][-1].next = node
            
        # 2. update the levels dictionary with current node
        self.levels[level].append(node)
        
        if not node:
            return
        
        # 4. recursive level order traverse
        if node.left:
            self.levelOrderTraverseRecursive(node.left, level+1)
        if node.right:
            self.levelOrderTraverseRecursive(node.right, level+1)
            
        return
        
    def connect(self, root: 'Node') -> 'Node':
        self.levels = {}
        #self.levelOrderTraverseIterative(root)
        self.levelOrderTraverseRecursive(root, 0)
        return root
