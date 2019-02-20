# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        # maintain record of visited subtree
        all_subtrees = {}
        # Root node results
        result = []

        def traverse(node):
            
            # Null node condition
            if not node:
                return "null"

            # Create subtree
            subtree_at_current_node = str(node.val)
            subtree_at_current_node += traverse(node.left)
            subtree_at_current_node += traverse(node.right)
                
            # Condition to handle already visited nodes
            if subtree_at_current_node in all_subtrees: 
                if all_subtrees[subtree_at_current_node] == 1:
                    result.append(node)
            else:
                all_subtrees[subtree_at_current_node] = 0
            # Increment visited nodes
            all_subtrees[subtree_at_current_node] += 1 
        
            # Return subtree to build for every node
            return subtree_at_current_node
        
        # Null node check
        if not root:
            return []
        
        traverse(root)
        
        return result
