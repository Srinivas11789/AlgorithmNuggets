# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        # Logic 1: 100% pass 100% time
        
        # Create a root prior
        root = TreeNode(preorder.pop(0))
        # Track all the parents as we visit
        parents = [root]
        # Iterate all the nodes in preorder
        while preorder:
            # Current value from preorder and its node representation
            current = preorder.pop(0)
            current_node = TreeNode(current)
            # If current is lesser, add to the left of the node
            if current < parents[-1].val:
                parents[-1].left = current_node
            else:
                # When the current is greater then remove all the nodes lesser than this node
                while parents and parents[-1].val < current:
                    last_node = parents.pop()
                # The last nodes right would be this 
                last_node.right = current_node
            # Append the node to parents list
            parents.append(current_node)
        return root
                
            
            
        
        """
        # Iterative method
        root = preorder.pop(0)
        parent = current_node = None
        while preorder:
            if current_node:
                parent = current_node
            current_node = TreeNode(preorder.pop(0))
            if current_node.val < root.val:
                root.left = current_node
                root = current_node
            elif parent and current_node.val > parent.val:
                root = parent
            else:
                root.right = current_node
                root = current_node
        
        
        def construct_tree(root_node, parent):
        
            if preorder:
                current_node = TreeNode(preorder.pop(0))
                if current_node.val < root_node:
                    root_node.left = current_node
                elif parent and root_node.val > parent.val:
                    return 
            else:
                return
        
        root = preorder.pop(0)
        construct_tree(root, preorder)
        
        return root
        """
