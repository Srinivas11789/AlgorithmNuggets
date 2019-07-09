# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        # Logic1: 
        # Recurse and
        # * Alter node to null if they are present in to_delete
        # * Each tree values on a list 
        # * If None, add the node value only if they have children
        # * Returns list of trees with node values list ( question asks for roots of the trees so alter logic)
        self.result = []
        
        def traverse(node, parent_value):
            if node.val in to_delete:
                node.val = None
            
            has_children = False
            
            if node.left or node.right:
                has_children = True
            
            if parent_value:
                if node.val or (node.val == None and has_children):
                    self.result[-1].append(node.val)
            else:
                #if self.result:
                #    self.result[-1].append([node.val])
                #else:
                    self.result.append([node.val])
                    
            if node.left:
                traverse(node.left, node.val)
                
            if node.right:
                traverse(node.right, node.val)
        
	# Logic: Modify above logic to only include root nodes in the result list
        # 100 pass
        def logic2(node, parent_value):
            
            if node.val in to_delete:
                node.val = None
            
            has_children = False
            
            if node.left or node.right:
                has_children = True
            
            if not parent_value and node.val:
                self.result.append(node)
                    
            if node.left:
                logic2(node.left, node.val)
                
            if node.right:
                logic2(node.right, node.val)
            
            if has_children and node.val == None:
                if node.left:
                    node.left = None
                if node.right:
                    node.right = None
            elif has_children:
                if node.left and node.left.val == None:
                    node.left = None
                if node.right and node.right.val == None:
                    node.right = None
                
        logic2(root, None)
        return self.result
"""
        # Logic: One time tree traversal with operations
        
        # Result list to hold the root nodes of the trees
        self.result = []
        
        # Helper method to recursively traverse all nodes (navigate the tree)
        def traverse(node, parent_value):
            
            # While we visit nodes in to_delete, alter their values to None
            # ( This lookup might take O(N), could be made faster)
            if node.val in to_delete:
                node.val = None
            
            # Check for children
            # - nodes who are parent and None should be included in the previous tree
            # - nodes who are parent and None should be removed from the relationship of its children
            has_children = False
            if node.left or node.right:
                has_children = True
            
            # Parent value if NULL include as separate tree
            if not parent_value and node.val:
                self.result.append(node)
                    
            # Traverse left and right children
            if node.left:
                traverse(node.left, node.val)
                
            if node.right:
                traverse(node.right, node.val)
            
            # Remove relationship of the None valued parent
            if has_children and node.val == None:
                if node.left:
                    node.left = None
                if node.right:
                    node.right = None
            elif has_children:
                # Check for tail leaf nodes ( output should not include leaf nodes that are None)
                if node.left and node.left.val == None:
                    node.left = None
                if node.right and node.right.val == None:
                    node.right = None
                
        traverse(root, None)
        return self.result
"""                
