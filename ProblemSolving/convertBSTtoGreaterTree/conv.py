# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 100 pass - with global variable
        # One Recursive Solution to change the values? 
        # 1. Only the left nodes and root require change the right nodes are meaningless to traverse
        # 2. Traverse right nodes and increase the total and add up with the left nodes 
        # Solution referece from joeytall
        """
        def greaterBST(root):
            if root:
                # Traverse right and add up all the right values
                greaterBST(root.right)
                self.total += root.val
                
                # Assign values to the left nodes from the right nodes
                root.val = self.total
                greaterBST(root.left)
                
            return root
        
        self.total = 0
        return greaterBST(root)
    
        """
        # 100 pass - without global variable
        
        def greaterBST(root, total):
            if root:
                # Traverse right and add up all the right values
                total = greaterBST(root.right, total)
                total += root.val
                
                # Assign values to the left nodes from the right nodes
                root.val = total
                total = greaterBST(root.left, total)
                
            return total
        
        total = 0
        greaterBST(root, total)
        return root
    
        """
        # Full Method - All pass but Time limit exceeded - optimize solution
        # 1. traverse the binary tree to get all the nodes - iteratively or recursive
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
        
        # 2. List of all the nodes
        print result
        
        # 3. Traverse again and change the value of the nodes
        def destinedValue(value):
            target = 0
            for val in result:
                if val > value:
                    target += val
            print value, target
            return target
        
        def change(node):
            if node:
                node.val += destinedValue(node.val)
                if node.left:
                    change(node.left)
                if node.right: 
                    change(node.right)
        
        change(root)
        return root
        """
        
