# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Logic 3
        # * Same traverse logic as 2, but calculate all possible values possible
        # * Compare
        #   - current max calculate based on the current path
        #   - current node value and left
        #   - current node value and right
        #   - current both left and right ( for instance when this only a root way path )
        #   - current node itself 
        
        # initial max value
        self.maxi = -float('inf')
        
        def traverse(node):
            
            # Calculate left and right sum
            left_sum = traverse(node.left) if node.left else 0
            right_sum = traverse(node.right) if node.right else 0
            
            # Calculate max as we defined
            self.maxi = max(self.maxi, node.val+left_sum, node.val+right_sum, node.val+left_sum+right_sum, node.val)
            
            # Return the path value as we traverse, compare with an additional "0", because we dont want a path which reduces the total path value
            return node.val + max(left_sum, right_sum, 0)
        
        traverse(root)
        
        return self.maxi
        
        """
        # Logic 2
        # * The challenge is to find any path that also goes without the root?
        # * A: To visualize such a logic, assume we always go from left to right to any node, then we use pre-order
        # * B1: After we do the preorder arrangement we then calculate the maximum path by another iteration
        # * B2: Improvise - We could also do a inbuilt iteration within the preorder loof itself.
        
        self.nodes_list = []
        self.maxi = -float('inf')
        sumi = 0
        
        def traverse(node, sumi):
            
            self.nodes_list.append(node.val)
            sumi += node.val
            
            if sumi > self.maxi:
                self.maxi = sumi
            
            if node.left:
                lsum = traverse(node.left, sumi)
            else:
                lsum = 0
            
            if node.right:
                rsum = traverse(node.right, lsum)
            else:
                rsum = 0
            
            return lsum + rsum
                
        traverse(root, sumi)
        return self.maxi
        """
        
        """
        # Logic 1
        # * PreOrder and Calculate 
        
        self.preorder_list = []
        
        def preorder_traverse(node):
            
            self.preorder_list.append(node.val)
            if node.left:
                preorder_traverse(node.left)
            if node.right:
                preorder_traverse(node.right)
                
        preorder_traverse(root)
        
        n = len(self.preorder_list)
        maxi = -float('inf')
        sumi = 0
        for i in range(n):
            print sumi, maxi
            sumi += self.preorder_list[i]
            if sumi > maxi:
                maxi = sumi
            else:
                sumi = self.preorder_list[i]
        return maxi
        """
            
            
        
        
