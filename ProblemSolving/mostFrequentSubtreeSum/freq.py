# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Logic 2: One tree traversal ==> 96% fast and 100% less storage
        # * Record all the subtree sums and add to dictionary
        # * calc max_freq from dictionary
        
        # frequency dictionary
        frequency = {}
        
        # calculate sum of all subtree and record them in dictionary
        def subtree_sum_calculate(node):
                
            # left subtree sum
            if node.left:
                left_sum = subtree_sum_calculate(node.left)
            else:
                left_sum = 0
                
            # right subtree sum
            if node.right:
                right_sum = subtree_sum_calculate(node.right)
            else:
                right_sum = 0
                 
            # calculate total subtree sum (root+left+right)
            subtree_sum_at_node = node.val + left_sum + right_sum
            
            # Add total sum (subtree_sum_at_node) to dictionary
            if subtree_sum_at_node not in frequency:
                    frequency[subtree_sum_at_node] = 0
            frequency[subtree_sum_at_node] +=1
                
            # Return sum of the subtree
            return subtree_sum_at_node
        
        # null check
        if not root:
            return []
        
        # function trigger
        subtree_sum_calculate(root)
        
        # Max freq 
        max_freq = max(frequency.values())
        result = []
        
        # Iterate dictionary for max freq items
        for k, v in frequency.items():
            if max_freq == v:
                result.append(k)
        
        return result
        
        
        """
        # Logic 1: Separate functions to take care of subtree sum calc and to traverse tree (kind of reptitive, implement better logic to perform this in one traversal) ==> 6% fast and 100% less storage
        
        # sums dictionary
        sums = {}
        
        # calculate sum of a subtree
        def subtree_sum_calculate(node):
                
            # left subtree sum
            if node.left:
                left_sum = subtree_sum_calculate(node.left)
            else:
                left_sum = 0
                
            # right subtree sum
            if node.right:
                right_sum = subtree_sum_calculate(node.right)
            else:
                right_sum = 0
                
            # Return sum of the subtree
            return node.val + left_sum + right_sum
        
        # Traverse to calculate subtree sum of each node as root
        def traverse(node):
            
            if node:
                subtree_sum_node = subtree_sum_calculate(node)
                if subtree_sum_node not in sums:
                    sums[subtree_sum_node] = 0
                sums[subtree_sum_node] +=1
            
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        # null check
        if not root:
            return []
        
        # function trigger
        traverse(root)
        
        # Max freq 
        max_freq = max(sums.values())
        result = []
        
        # Iterate dictionary for max freq items
        for k, v in sums.items():
            if max_freq == v:
                result.append(k)
        
        return result
        """
        
