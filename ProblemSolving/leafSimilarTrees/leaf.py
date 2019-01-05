# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        # Dictionary to store the value of the leaves for each tree
        self.leaves = {
            root1: [],
            root2: []
        }
        
        # Null check
        if not root1 or not root2:
            return False
        
        # Traverse tree function
        def get_leaves(root, node):
            
            # debug
            """
            print node.val
            if node.left:
                print node.left.val
            if node.right:
                print node.right.val
            print "debug end!"
            """
            
            # When node is None check
            if not node:
                return
            
            # detect Children
            if node.left == None and node.right == None:
                self.leaves[root].append(node.val)
            
            # Traverse nodes (Lesson: Use if loops not elif/else as it looks for only one possibility as we traverse)
            if node.left:
                get_leaves(root, node.left)
            if node.right:
                get_leaves(root, node.right)

        
        get_leaves(root1, root1)
        get_leaves(root2, root2)
        
        # Debug
        #print self.leaves[root1], self.leaves[root2]
        
        if self.leaves[root1] == self.leaves[root2]:
            return True
        else:
            return False
        
        #else:
        # leaf ==> [node.left == None and node.right == None]
        #    self.leaves[root].append(node.val)
