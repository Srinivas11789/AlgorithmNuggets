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
        
        # Recursive method
        def recurse(array):
            
            if not array:
                return
            
            # Select maximum and compute left and right subtree
            maxi = max(array)
            maxi_ind = array.index(maxi)
            left = array[:maxi_ind]
            right = array[maxi_ind+1:]
            
            # Create a node
            node = TreeNode(maxi)
            
            # Add left and right to each node
            node.left = recurse(left)
            node.right = recurse(right)
            
            # return node so the tree is build as we recurse
            return node
        
        # Iterative method
        # * the list persistence (left,right) could have been done better. The indexes get corrupted between array, left, right hence stored the node with the corresponding next array to operate
        def iterative(array):
            
            # Select maximum and create root
            maxi = max(array)
            root = TreeNode(maxi)
            
            # Stack to track the traversal - Storing the node with the corresponding array to operate next.
            # * Find some way to persist array, indexes across iteration
            stack = [(root, array)]
            
            # Iterate through all the nodes
            while stack:
                # pop 0 as per breath first traversal
                current = stack.pop(0)
                
                # Extract the node and corresponding array
                current_node = current[0]
                array = current[1]
                
                # Debug
                #print current_node.val, array
                
                # Maximum index and left and right sub array
                index = array.index(current_node.val)
                left = array[:index]
                right = array[index+1:]
                
                # Operate on left
                # * Create node, Add left node and then to stack to continue traversal
                if left:
                    left_node = TreeNode(max(left))
                    current_node.left = left_node
                    stack.append((left_node, left))
                
                # Operate on right
                # * Create node, Add right node and then to stack to continue traversal    
                if right:
                    right_node = TreeNode(max(right))
                    current_node.right = right_node
                    stack.append((right_node, right))
            
            return root
        
        # Recursive Solution
        # Function call and return
        root = recurse(nums)
        return root
        
        # Iterative solution
        #return iterative(nums)
        
        
        """
        # Plain thinking
        maxi = max(nums)
        root_index = nums.index(maxi)
        root = TreeNode(nums[root_index])
        
        left = nums[:root_index]
        right = nums[root_index+1:]
        
        while left:
            maxi = max(left)
        """
            
