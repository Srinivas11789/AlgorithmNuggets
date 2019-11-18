"""
Given a tree, find if the binary tree is height balanced or not. A height balanced binary tree is a tree where every node's 2 subtree do not differ in height by more than 1.

Here's some starter code:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def is_height_balanced(tree):
  # Fill this in.

#     1
#    / \
#   2   3
#  /
# 4  
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    / 
#   2   
#  /
# 4  
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def find_height(node):
    if not node:
      return -1
    else:
      return 1 + max(find_height(node.left), find_height(node.right))

def is_height_balanced(tree):
 
  if tree.left:
      is_height_balanced(tree.left)
  if tree.right:
      is_height_balanced(tree.right)
 
  if abs(find_height(tree.right)-find_height(tree.left)) <= 1:
    return True
  else:
    return False

#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
