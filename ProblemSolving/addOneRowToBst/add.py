# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        # Logic: 40ms 97% --> get to the correct depth insert based on the parent and current node (create a new node and then insert)
        def getToDepthAndInsert(node, current_depth, parent):
            
            # If the current depth is reached, then create new node
            if current_depth == d:
                new_node = TreeNode(v)
                # * If the corresponding depth is greater than the leaf, then add as leaf
                # * Else, insert in between
                if not node:
                    if not parent.left:
                        parent.left = new_node
                    elif not parent.right:
                        parent.right = new_node
                else:
                    if parent.left == node:
                        parent.left = new_node
                        new_node.left = node
                    else:
                        parent.right = new_node
                        new_node.right = node
            else:
                # If depth is not reached, recurse
                if node:
                    getToDepthAndInsert(node.left, current_depth+1, node)
                    getToDepthAndInsert(node.right, current_depth+1, node)
        
        # Depth being the root itself
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            root = new_node
        else:
            getToDepthAndInsert(root, 1, None)
        
        return root
        
        
