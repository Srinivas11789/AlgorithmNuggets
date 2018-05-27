# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Logic:
        # 1. Traverse the BST - Breath First Search
        if not root:
            return []
        
        nodes = [root]
        result = []
        
        while len(nodes) > 0:
            current = nodes.pop(0)
            result.append(current.val)
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)
                
        # 2. Make a list of all node values
        print result
        
        # 3. Iterate through the list and negate a number and find the remaining existence in the list for the answer
        for i in range(len(result)):
            value = k-result[i]
            # Neglect the selected current node and test the presence in the remaining array
            if value in result[:i]+result[i+1:]:
                return True
        return False
