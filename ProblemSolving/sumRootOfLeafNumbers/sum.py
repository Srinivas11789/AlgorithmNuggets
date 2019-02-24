# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node, number):
            
            if not node.left and not node.right:
                self.leaf_nums.append(int(number))
            else:
                if node.left:
                    traverse(node.left, number+str(node.left.val))
                if node.right:
                    traverse(node.right, number+str(node.right.val))
        
        self.leaf_nums = []
        if not root:
            return 0
        traverse(root, str(root.val))
        print self.leaf_nums
        return sum(self.leaf_nums)
            
            
        
