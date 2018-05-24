# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(root):
            
            if not root:
                return 
            
            nodes = []
            result = []
            current = root
            
            while 1:
                if current:
                    nodes.append(current)
                    current = current.left
                else:
                    if len(nodes) > 0:
                        current = nodes.pop()
                        result.append(current.val)
                        current = current.right
                    else:
                        break
            return result
    
        all_nodes = traverse(root)
        mini = float("inf")
        for i in range(1,len(all_nodes)):
            mini = min(mini, abs(all_nodes[i]-all_nodes[i-1]))
        return mini
