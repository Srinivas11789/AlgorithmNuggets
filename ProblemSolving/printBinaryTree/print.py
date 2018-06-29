# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Logic Reference from yjlchina - 100 pass
# Steps:
# * Construct the array of all the levels
#     - Find the height of the BST
#     - Fill all the levels with null values in a iterative fashion for h levels and nodes (2pow(h)-1 number of leaf nodes)
# * Iterate the binary search tree with traversing the nodes with left and right calculation and fill in the midpoint

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def height(root):
            if not root:
                return 0
            else:
                return 1+max(height(root.left),height(root.right))
            
        """
        # Level Order Search
        if not root:
            return None
        
        nodes = []
        result = []
        
        while nodes:
            n = len(nodes)
            result.append([])
            while n > 0:
                current = nodes.pop()
                if current.val:
                    result[-1].append(current.val)
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)
                n -= 1
        """
        
        h = height(root)
        right = 2**h - 1
        
        levels  = [[""]*right for x in range(h)]
        
        traverse = [(root, 0, 0, right)]
        for n in traverse:
            node, i, l, r = n[0], n[1], n[2], n[3]
            j = (l+r)//2
            levels[i][j] = str(node.val)
            if node.left:
                traverse.append((node.left, i+1, l, j))
            if node.right:
                traverse.append((node.right, i+1, j, r))
        return levels
        
        
        
