# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Boil down to the fundamental - Symmetry is when the tree is mirror of itself
        # That means, in a tree
        # For a node when both the chidren dont exist pass
        # When both the children exist with the same value pass
        # When one of the child exist, the left of one child should be equal to right of another child and viceversa
        # Everytime you iterate or append for the loop traversal to move forward ---> use symmtery rule, pair up node1.right, node2.left and node1.left, node2.right
        
        if not root:
            return True
        
        nodes = [(root.left,root.right)]
        
        while nodes:
                left,right = nodes.pop(0)
                
                if not left and not right:
                    pass
                elif left and not right:
                    return False
                elif right and not left:
                    return False
                elif left.val != right.val:
                    return False
                else:
                    # Matching criteria as per symmetry
                    nodes.append((left.right, right.left))
                    nodes.append((left.left, right.right))
                    
        return True    
        
        """
        def inOrder(node, memo):
            if not node:
                return
            else:
                if node.left and node.right:
                    inOrder(node.left, memo)
                    memo.append(node.val)
                    inOrder(node.right, memo)
                elif node.left:
                    inOrder(node.left, memo)
                    memo.append(node.val)
                    memo.append(None)
                elif node.right:
                    memo.append(None)
                    memo.append(node.val)
                    inOrder(node.right, memo)
        
        memo = []
        inOrder(root, memo)
        print memo
        """
        
        """
        if not memo:
            return True
        
        left = 0
        right = -1
        print memo
        while left < len(memo)+right:
            if memo[left] == memo[right]:
                print left, right
                memo.pop(left)
                memo.pop(right)
            else:
                left += 1
                right -= 1
        if len(memo) == 1:
            return True
        else:
            return False
        """  
        
