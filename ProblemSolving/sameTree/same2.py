# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Recursive method ( any traversal pre/post/in or bfs can be used )
        
        # 1. Go through the full recursion of both the trees separately and then decide - 100 pass
        """
        def preOrder(node, order):
            if node:
                order.append(node.val)
                if node.left:
                    preOrder(node.left, order)
                else:
                    order.append(None)
                if node.right:
                    preOrder(node.right, order)
                else:
                    order.append(None)
            return order
        
        return preOrder(p, []) == preOrder(q, [])
        """
        
        # 2. Go through both the trees together in single iteration, as soon as there is a mismatch exit - 100 pass
        """
        def traverse(node1, node2):
            
            # one of the nodes is null
            current = False
            if not node1 and not node2: # both are null
                current = True
            elif node1 and node2: # both are not null
                
                # Current node
                if node1.val != node2.val:
                    current = False
                else:
                    current = True

                # Left Node
                if node1.left and node2.left:
                    current &= traverse(node1.left, node2.left)
                elif not node1.left and not node2.left:
                    current &= True
                else:
                    current &= False

                # Right Node
                if node1.right and node2.right:
                    current &= traverse(node1.right, node2.right)
                elif not node1.right and not node2.right:
                    current &= True
                else:
                    current &= False
                    
            return current
        
        return traverse(p, q)
        """
        
        # Iterative Method - 100 pass
        
        # Create 2 stacks to track the nodes in both the trees
        tree1 = [p]
        tree2 = [q]
        
        # Iterate until both the nodes in trees expire together...
        while tree1 and tree2:
            
            # Current Node check
            t1 = tree1.pop(0)
            t2 = tree2.pop(0)
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                
                # Add left and right of both the trees
                tree1.append(t1.left) if t1.left else tree1.append(None)
                tree1.append(t1.right) if t1.right else tree1.append(None)
                tree2.append(t2.left) if t2.left else tree2.append(None)
                tree2.append(t2.right) if t2.right else tree2.append(None)
            elif not t1 and not t2: # Continue if both are None
                pass
            else: # Fail if one of them is None
                return False
            
        # If one tree still remains then False
        if tree1 or tree2:
            return False
        else:
            return True

        
        
