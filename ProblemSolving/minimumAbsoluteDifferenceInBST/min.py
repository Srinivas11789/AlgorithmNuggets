# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #Logic2: Recursive - 100 pass
        
        # InOrder traversal sorts the nodes
        def inOrderTraverse(node):
            if not node:
                return
            
            if node.left:
                inOrderTraverse(node.left)
            values.append(node.val)
            if node.right:
                inOrderTraverse(node.right)
        
        values = []
        # In order traversal fills the values with sorted nodes
        inOrderTraverse(root)
        print values
        mini = float('inf')
        
        # Iterate the values sorted array for the minimum
        for i in range(len(values)-1):
            if abs(values[i]-values[i+1]) < mini:
                mini = abs(values[i]-values[i+1])
        
        return mini
        
        
        """
        # Logic1: Iterative - 100 pass
        
        # Traverse and store the values in an array 
        if not root:
            return 0
        
        nodes = [root]
        mini = float('inf')
        values = []
        
        while nodes:
            node = nodes.pop()
            values.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
                
        # Sort the values so the consecutive values line up - min values are between the closest elements
        values.sort()
        
        # Iterate the values sorted array for the minimum
        for i in range(len(values)-1):
            if abs(values[i]-values[i+1]) < mini:
                mini = abs(values[i]-values[i+1])
        
        return mini
        """
                
        """
        # Doesnt work when consecutive integers exists initialy or middle
        if len(values) > 1:
            mini = abs(values[-1] - values[-2])
        else:
            mini = values[0]
        """
