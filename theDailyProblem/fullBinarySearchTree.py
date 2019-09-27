"""
Given a binary tree, remove the nodes in which there is only 1 child, so that the binary tree is a full binary tree.

So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.

Here's a starting point:

from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result

def fullBinaryTree(node):
  # Fill this in.

# Given this tree:
#     1
#    / \ 
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \ 
#   0   3
#      / \
#     9   4

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print fullBinaryTree(tree)
# 1
# 03
# 94
"""
from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result


# This wont work as we progress some node in a single node subtree might be complete, we need to find that and connect properly
# Add altered function with parent argument to fix this

# Logic1: With parent argument
def fullBinaryTree(node, parent):
  # Remove single nodes prior to avoid traversing them
  if node.left and not node.right:
      parent.left = node.left
      fullBinaryTree(node.left, parent)
  elif not node.left and node.right:
      parent.right = node.right
      fullBinaryTree(node.right, parent)
  else:
    # Traverse the binary search tree
    if node.left:
      fullBinaryTree(node.left, node)
    if node.right:
      fullBinaryTree(node.right, node)
  
  return node

# Logic 2: Without parent argument

def main():
  tree = Node(1)
  tree.left = Node(2)
  tree.right = Node(3)
  tree.right.right = Node(4)
  tree.right.left = Node(9)
  tree.left.left = Node(0)
  print fullBinaryTree(tree, tree)

main()
