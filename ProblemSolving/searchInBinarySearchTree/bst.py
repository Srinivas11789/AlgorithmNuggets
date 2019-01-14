# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 100 pass 
        # traverse level order using a list
        stack = [root]
        
        # Bool to find a match
        match = 0
        
        # result tree
        self.result = []
        
        # Traverse by popping as we move
        while stack:
                # Current element from front of the list
                current = stack.pop(0)
                # Null check
                if current:
                    # Match!, then update stack and match var
                    if current.val == val:
                        stack = []
                        self.result = []
                        match = 1
                    
                    # If match happened then append to result
                    if match == 1:
                        self.result.append(current.val)
                        
                    # Traversing update for left and right of current node
                    stack.append(current.left)
                    stack.append(current.right)
                else:
                    # Result expects addition of null for nodes that are null
                    self.result.append(None)
        
        # Eradicate nulls present at the end
        while self.result and self.result[-1] == None:
            self.result.pop()
                
        return self.result
        
        """
        # Expected answer in level order traversal
        self.selected = None
        self.subtree = []
        
        # Recursive
        def recurse(node):
            
            if not node:
                #self.subtree.append(None)
                return
            
            self.subtree.append(node.val)
            
            if node.val == val:
                self.selected = node
            
            if not node.left and not node.right:
                return

            if node.left:
                recurse(node.left)
            else:
                self.subtree.append(None)
            
            if node.right:
                recurse(node.right)
            else:
                self.subtree.append(None)
                
        recurse(root)
        
        if self.selected:
            self.subtree = []
            recurse(self.selected)
            return self.subtree
        else:
            return None
        """
        
        
