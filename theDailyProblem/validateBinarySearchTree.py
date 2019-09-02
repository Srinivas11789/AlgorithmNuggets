"""
You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  # Fill this in.

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print is_bst(a)

#    5
#   / \
#  3   7
# / \ /
#1  4 6

"""

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

# Maintain all ancestors and check it supports BST property
# * less than the root if left 
# * greater than the root if right
# Summary
# * For each node, it should be greater if right or lesser if left for all nodes in subtree except root


# Break down the logic to avoid confusion
# * Logic to get all the left and the right subtree of each node
"""
def is_bst(node):
  # Condition to recurse
  left_subtree = right_subtree = []
  if node.left:
    left_subtree = is_bst(node.left)
  if node.right:
    right_subtree = is_bst(node.right)
  print(left_subtree, right_subtree)
  if node:
    path = [node.key] + left_subtree + right_subtree
  return path
"""

def is_bst(node):
  # Condition to recurse
  left_subtree = right_subtree = []
  lresult = rresult = True
  if node.left:
    left_subtree, lresult = is_bst(node.left)
  if node.right:
    right_subtree, rresult = is_bst(node.right)
  print(left_subtree, right_subtree)
  for l in left_subtree:
    if l > node.key:
      lresult = False
  for r in right_subtree:
    if r < node.key:
      rresult = False
  if node:
    path = [node.key] + left_subtree + right_subtree
  return path, lresult and rresult

def main():
  a = TreeNode(5)
  a.left = TreeNode(3)
  a.right = TreeNode(7)
  a.left.left = TreeNode(1)
  a.left.right = TreeNode(8)
  a.right.left = TreeNode(6)
  print is_bst(a)[1]  

main() 
