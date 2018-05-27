# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Recursive mode - 100 pass 
        # 1. The method already implemented uses a array to track the list of tilts
        # 2. Another method is to use a global variable to add up recursively to it like self.tilt
        # 3. Some nice method have been implemented in discussions where a tuple to track the sum and current sum of tilts could be returned
        
        def tilt(node):
            
            if not node:
                return 0
            else:
                
                # Recurse to traverse through the nodes
                left = tilt(node.left)
                right = tilt(node.right)
                
                # Tilt at each node
                tilts.append(abs(left-right))
            
                # To return the sum of the subtree as a whole for further calculation as we move back upward
                return node.val + left + right 
                
        tilts = []
        tilt(root)
        print tilts
        return sum(tilts)
        
    
        """    
        # Iterative Method - 100 pass - reference from luffyzhou
        
        # Use a stack data structure to store the indicator and node - Control Variable
        # indicator is to track the expansion of corres node to left and right
        stack = [(1,root)]
        
        # result variables - dictionary to track the sum of the subtree per node 
        tilt, d = 0, {None:0}
        
        # Unless stack expires
        while stack:
            
            # Stack operation
            indicator, node = stack.pop()
    
            # None condition - handled in the dict
            if not node:
                continue
            
            # If indicator make the corres node indicator 0 to process and add left and right with indicator 1
            if indicator:
                stack.extend([(0,node), (1,node.left), (1,node.right)])
            else:
                # Tilt calculation as we progress
                tilt += abs(d[node.left]-d[node.right])
                
                # Sum tracking for all the nodes in the dictionary
                d[node] = node.val+d[node.left]+d[node.right]
                
        return tilt
        """
        
        
        
