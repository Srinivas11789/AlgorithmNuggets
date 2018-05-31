# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        # Logic 2: 100 pass - At each node perform a inOrder traversal and compare
        # At each node find its tree using inOrder traversal and match with the other tree inOrder traversal
        # * Doing it for each node rather than the full tree will easily match exactly and return True
        
        def inOrder(node, values, mode):
            if not node:
                return 
            else:
                if node.left:
                    inOrder(node.left, values, mode)
                if mode == 1:
                    values.append(node)
                else:
                    values.append(node.val)
                if node.right:
                    inOrder(node.right, values, mode)
        
        # Get the inOrder traversal VALUES of the tree2
        values1 = []
        inOrder(s, values1, 1)
        # Get the inOrder traversal NODES of the tree1
        values2 = []
        inOrder(t, values2, 0)
        
        # Iterate through the nodes of tree1 and perform inOrderTraversal of VALUES for each node as root and match with the tree2 VALUES 
        for node in values1:
            value = []
            # Reduces the recursion and speeds up
            if node.val == t.val:
                inOrder(node, value, 0)
                if value == values2:
                    return True
        return False
        
        
        """
        # Logic 3: 100 pass - Try to match the root of tree2 with any node and start comparing from there
        
        def subTree(tree1, tree2):
            
            if not tree1 and not tree2:
                return True
            
            if not tree1 or not tree2:
                return False
                
            if tree1.val == tree2.val:
                tree1_left = tree1_right = None
                tree2_left = tree2_right = None
                
                if tree1.left:
                    tree1_left = tree1.left.val
                if tree1.right:
                    tree1_right = tree1.right.val
                if tree2.left:
                    tree2_left = tree2.left.val
                if tree2.right:
                    tree2_right = tree2.right.val
                    
                if (tree1_left == tree2_left and tree1_right == tree2_right) and (subTree(tree1.left, tree2.left) and subTree(tree1.right, tree2.right)):
                    return True
            
            return subTree(tree1.left, tree2) or subTree(tree1.right, tree2)    
                    
        return subTree(s,t)
        """
        
        """
        # Logic 1: Perform a traversal of both trees and check the match
        # Works but sometimes order gets crapped when null nodes occurs in a tree
        
        if not s or not t:
            return False
        
        nodes = [s]
        values1 = []
        nodes1 = [t]
        values2 = []
         
        
        # Traverse together
        while nodes and nodes1:
            node1 = nodes.pop(0)
            node2 = nodes1.pop(0)
            values1.append(node1.val)
            values2.append(node2.val)
            if node1.left:
                nodes.append(node1.left)
            if node1.right:
                nodes.append(node1.right)
            if node2.left:
                nodes1.append(node2.left)
            if node2.right:
                nodes1.append(node2.right)
        
        # Traverse remaining
        while nodes: 
            node1 = nodes.pop(0)
            values1.append(node1.val)
            if node1.left:
                nodes.append(node1.left)
            if node1.right:
                nodes.append(node1.right)
        
        while nodes1:
            node2 = nodes1.pop(0)
            values2.append(node2.val)
            if node2.left:
                nodes1.append(node2.left)
            if node2.right:
                nodes1.append(node2.right)
        
        print values1, values2
        
        i = 0 
        n = len(values2)
        while i < len(values1): 
            if values1[i] in values2:
                values2.pop(values2.index(values1[i]))
                i += 1
            else:
                values1.pop(i)
        
        print values1, values2
        
        if len(values1) != n:
            return False
        else:
            return True
        """        
        
        
        
