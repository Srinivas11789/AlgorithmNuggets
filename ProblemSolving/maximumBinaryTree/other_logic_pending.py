#### Pending...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # Finding the root
        root = max(nums)
        rootIndex = nums.index(root)
        
        # Create a tree
        rootNode = TreeNode(root)
        
        # Left and the Right Subarray
        left = nums[:rootIndex]
        right = nums[rootIndex+1:]
        
        # First left and the right node
        if len(left) >= 1:
            rootNode.left = TreeNode(max(left))
            leftTree = rootNode.left
        if len(right) >= 1:
            rootNode.right = TreeNode(max(right))
            rightTree = rootNode.right
            
        count = len(left)-1
        while count > 0:
            maxi = left.index(leftTree.val)
            l = left[:maxi]
            r = left[maxi+1:]
            left.pop(maxi)
            if len(l) >= 1:
                leftTree.left = TreeNode(max(l))
                leftTree = leftTree.left
                count -= 1
            if len(r) >= 1:
                leftTree.right = TreeNode(max(r))
                leftTree = leftTree.right
                count -= 1
                
        
        count = len(right)-1
        while count > 0:
            maxi = right.index(rightTree.val)
            l = right[:maxi]
            r = right[maxi+1:]
            right.pop(maxi)
            if len(l) >= 1:
                rightTree.left = TreeNode(max(l))
                rightTree = rightTree.left
                count -= 1
            if len(r) >= 1:
                rightTree.right = TreeNode(max(r))
                rightTree = rightTree.right
                count -= 1
        
        return rootNode
        """
        # This logic is with respect to a bst - problem statement works on the maximum element
        
        # Left and the Right Subtree split
        left = sorted(nums[:rootIndex], reverse=True)
        right = sorted(nums[rootIndex+1:],reverse=True)
        
        # First left and the right node
        if len(left) >= 1:
            rootNode.left = TreeNode(left[0])
            leftTree = rootNode.left
        if len(right) >= 1:
            rootNode.right = TreeNode(right[0])
            rightTree = rootNode.right
        
        if len(left[1:]) > 1:
            # Iterate to fill in every node
            for num in left[1:]:
                if num > leftTree.val:
                    leftTree.left = TreeNode(num)
                    leftTree = leftTree.left
                else:
                    leftTree.right = TreeNode(num)
                    leftTree = leftTree.right
        
        if len(right[1:]) >= 1:
            for num in right[1:]:
                if num < rightTree.val:
                    rightTree.left = TreeNode(num)
                    rightTree = rightTree.left
                else:
                    rightTree.right = TreeNode(num)
                    rightTree = rightTree.right
        
        return rootNode
        """       
        
        
