# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        
        # 100 pass
        # A general traversal to retrieve all the nodes into a list - Traverse and then operate
        def traverse(node):
            if not node:
                return None
            else:
                nodes.append(node.val)
                traverse(node.left)
                traverse(node.right)
                
        # List to hold all the node values
        nodes = []
        # Traverse and fill all the nodes
        traverse(root)
        
        # Eradicate duplicate node values
        nodes = list(set(nodes))
        # Sort the nodes in ascending order
        nodes.sort()
        # Debug
        print nodes
        # as the question mentions k will always be valid within BST elements, we need not check for k invalidity
        return nodes[k-1]
        
            
