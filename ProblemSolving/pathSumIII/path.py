# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        # Logic:
        # We require to use 2 recursion loops as we need to arrive at the sum from any node
        # 1st loop --> to traverse through the nodes
        # 2nd loop --> to calculate the path sum at each node
        #
        
        # 2nd loop - pathSum
        def pathSum(node, total, sum):
            if not root:
                return 
            total += node.val
            if total == sum:
                self.count += 1       
            if node.left:
                pathSum(node.left, total, sum)
            if node.right:
                pathSum(node.right, total, sum)
        
        # 1st loop - traverse
        def traverse(root):
            if root:
                pathSum(root, 0, sum)
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)
            return
        
        self.count = 0
        traverse(root)
        return self.count
        
        """
        # Wrong Method
        if not root:
            return 0
        
        total = 0
        nodes = [root]
        count = 0
        
        while nodes:
            current = nodes.pop(0)
            print current.val, total
            total += current.val
            if total > sum or total < sum:
                total = 0
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)
            if total == sum:
                count += 1
                
        return count
        """
