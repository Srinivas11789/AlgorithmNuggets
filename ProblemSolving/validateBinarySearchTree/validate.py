# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Logic 1: 92 ms, 6.75% faster and 5.66% space
        
        # * Get left and right subtree for each node
        # * Check if the bst condition is satisfied ( left subtree is less and right subtree is greater )
        
        """
        # Recursive function to return the subtree (path) and check for bst satisfaction
        def isBst(node):
            
            # Node Null condition and empty tree condition
            if not node:
                return [], True
            
            # Initialize variables to use
            left_subtree = right_subtree = []
            lresult = rresult = True
            
            # Condition to recurse
            if node.left:
                left_subtree, lresult = isBst(node.left)
            if node.right:
                right_subtree, rresult = isBst(node.right)
                
            # BST conditon check, for each node, left subtree is less and right subtree is greater
            for l in left_subtree:
                if l >= node.val:
                    lresult = False
            for r in right_subtree:
                if r <= node.val:
                    rresult = False
                    
            # Add current node to path for returning subtree
            if node:
                path = [node.val] + left_subtree + right_subtree
            
            # Debug
            #print(left_subtree, right_subtree, path, lresult, rresult)
            
            # Exit function with returning subtree and result
            return path, lresult and rresult
        
        # Get the subtree and result 
        tree, result = isBst(root)
        
        return result
        """
     
        # Logic 2: 6% faster
        # * Take the in-order traversal of the tree and check if they are sorted
        
        # Function for in-order traversal
        def in_order_traverse(node):
            
            if node:
                # In Order Traverse
                # First LEFT
                if node.left:
                    in_order_traverse(node.left)
                    
                # This challenge works under the assumption that BST does not have duplicates
                # Find duplicates
                if node.val in self.in_order_arrangement:
                    self.duplicate = True
                    return False
                
                # THEN ROOT
                self.in_order_arrangement.append(node.val)

                # NEXT RIGHT
                if node.right:
                    in_order_traverse(node.right)
            else:
                return
        
        self.duplicate = False
        self.in_order_arrangement = []
        in_order_traverse(root)
        
        # Duplicate node values existence
        if self.duplicate:
            return False
        
        # Debug
        #print(self.in_order_arrangement, sorted(self.in_order_arrangement), list(set(self.in_order_arrangement)))
        
        # If arrangement is already in the sorted form from left to right then it is a valid BST
        if sorted(self.in_order_arrangement) == self.in_order_arrangement:
            return True
        else:
            return False
