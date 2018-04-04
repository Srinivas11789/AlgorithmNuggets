# Some notes from geeks of geeks for binary search tree 
# more @ https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
"""
Following are common types of Binary Trees.

Full Binary Tree A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree. We can also say a full binary tree is a binary tree in which all nodes except leaves have two children.

Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible

Perfect Binary Tree A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
Following are examples of Perfect Binaryr Trees.

Balanced Binary Tree
A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. For Example, AVL tree maintain O(Log n) height by making sure that the difference between heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
"""

# Binary Search Tree Construction and Logic

class node:
	
	def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

	def print_node(self):
            print(self.value, self.right, self.left)


# Full Binary Search Tree Problem

def isFullBinarySearchTree(node):
    #print node.value
    #return isFullBinarySearchTree(node.left) and isFullBinarySearchTree(node.right)
    #print node.value
    #if (node.left == None and node.right == None) or (node.left and node.right):
    #   return True

    # While using recursive function always place the failure cases and deep level true cases check before the recursion loop of return. If positive case exists then the initial level becomes true and causes exit. Recursion => Failure Cases => Return Recursion loop

    if node is None:
       return True
    if not node.left or not node.right:
       if node.left == None and node.right == None:
          pass
       else:
      	  return False
    return isFullBinarySearchTree(node.left) and isFullBinarySearchTree(node.right)

# Complete Binary Search Tree

def numberOfNodes(node):
    if node is None:
       return 0
    return (1 + numberOfNodes(node.left) + numberOfNodes(node.right))

def completeBinarySearchTree(node, index, number_of_nodes):
    """
    # Method not complete, idea or outline only
    # Goto to the deepest node
    if node is None:
	return True:
    # Last level of nodes could have no children or some children aligned to the left
     if not node.left or not node.right:
       if node.left == None and node.right == None:
          pass
       else:
          # Check for left alignment of nodes
          return False
    return completeBinarySearchTree(node.left) and completeBinarySearchTree(node.right)
    """

    # One method from Geek of Geek to keep track of index and the number of nodes

    # Basically the idea of this method is to mark the nodes with indexes as follows
    # * root = 3 = 0
    #   * left = 1 = 1
    #   * right = 4 = 2
    # from left to right each node continues with 3,4,5
    # With the total number of nodes known already, just tracking the indexes not to exceed or equal to one of the nodes is enough to hit a failure condition
    # Outline is to get the total nodes and number each nodes from left to right to track it thus the second property of left heavy tree or leaves in the last level all are to the left side passes including the no leaf condition as well

    # Deepest level when node becomes none
    if node is None:
	return True
    # if the index is more than the total number of nodes in the tree
    if index >= number_of_nodes:
        return False
    print index, node.value
    return (completeBinarySearchTree(node.left, 2*index+1, number_of_nodes)) and (completeBinarySearchTree(node.right, 2*index+2, number_of_nodes))
    

# Perfect Binary Search Tree

# Balanced Binary Search Tree

def main():
    root = node(3)
    root.left = node(1)
    root.left.left = node(0)
    root.left.right = node(2)
    root.right = node(4)
    #root.right.right = node(5)
    root.right.left = node(3)
    print isFullBinarySearchTree(root)

    # Complete BST
    n = numberOfNodes(root)
    print n
    print completeBinarySearchTree(root, 0, n)

main()
