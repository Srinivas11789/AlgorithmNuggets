# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Logic 1: Recursive traverse - 100 pass 63% faster
        
        # Collect all the path in binary in a list
        self.path_to_leaf = []
        # Track total binary sum and return result
        self.total_binary_sum = 0
        
        # Traverse tree function
        def traverse(node, path):
            # If not leaf node, record the path left or right
            if node.left:
                traverse(node.left, path+str(node.val))
            if node.right:
                traverse(node.right, path+str(node.val))
            
            # Leaf node detect and record path
            if not node.left and not node.right:
                path += str(node.val)
                self.path_to_leaf.append(path)
                self.total_binary_sum += int(path, 2)
        
        traverse(root, "")
        print(self.path_to_leaf)
        return self.total_binary_sum
        
        
        # Logic 2: Iterative method - 100 pass 83 percent faster
        # * Each element of the list has the node and the path to it
        """
        stack = [[root, ""]] # iteration to keep track
        result = 0 # result holder
        
        # Traverse nodes by stacking them
        while stack:
            # current node and path tracking
            current, path = stack.pop(0)
            
            # traverse with path 
            if current.left:
                stack.append([current.left, path+str(current.val)])
            if current.right:
                stack.append([current.right, path+str(current.val)])
            
            # leaf node condition when we update result
            if not current.left and not current.right:
                path += str(current.val)
                result += int(path, 2)
                
        return result
        """
            
        
