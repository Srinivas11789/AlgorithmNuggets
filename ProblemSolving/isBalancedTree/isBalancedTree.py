# Binary Search Tree

# 100 pass
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(node):
            
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left < 0 or right < 0 or abs(left-right) > 1:
                return -1
            return 1+max(left, right)
    
        if height(root) >= 0:
            return True
        else:
            return False
        
        """
        def height(node):
            
            if node is None:
                return 0
            else:
                return 1+max(height(node.left), height(node.right))
        
        def balance(node):
            
            if node is None:
                return result
            else:
                if node.left:
                        balance(node.left)
                if node.right:
                        balance(node.right)
                if abs(height(node.left)-height(node.right)) <= 1:
                    return True
                else:
                    return False
        
        if not root:
            return True

        return balance(root)
        """
        

"""
# This solution is not correct

#### Class Node to hold the structure of each node

class node:

      def __init__(self, value, left, right):
	self.value = value
	self.left = left
	self.right = right


def height(node):
    if node is None:
       return -1
    else:
       return max(height(node.left),height(node.right))+1

def balancedSubtree(root):
    if root == None:
       return 0;
    left = balancedSubtree(root.left)
    right = balancedSubtree(root.right)
    if left<0 or right<0 or abs(left-right)>1:
       return -1
    return max(left,right)+1


def main():
    root = node(1,None,None)
    root.left = node(2,None,None)
    root.right = node(3,None,None)
    print root.value
    print root.left
    print height(root)
    print balancedSubtree(root)

main()
"""
