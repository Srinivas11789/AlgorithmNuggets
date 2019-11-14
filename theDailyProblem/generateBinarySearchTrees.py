# One hacky recursive way to work...
"""
Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.

Here's some code to start with:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    result = str(self.value)
    if self.left:
      result = result + str(self.left)
    if self.right:
      result = result + str(self.right)
    return result

def generate_bst(n):
  # Fill this in.

for tree in generate_bst(3):
  print tree

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
"""
import copy
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    result = str(self.value)
    if self.left:
      result = result + str(self.left)
    if self.right:
      result = result + str(self.right)
    return result

def generate_bst(n):
  trees = []
  ns = range(1, n+1)
  def construct_tree(nodes, parent, ancestor):
      if not nodes:
          return
      for i in range(len(nodes)):
        #print("hi", parent)
        root = Node(nodes[i])
        if parent == None:
          ancestor = root
        if parent and root.value < parent.value:
           parent.left = root
        elif parent:
           parent.right = root
        left = nodes[:i][::-1]
        right = nodes[i+1:]
        if left:
          construct_tree(left, root, ancestor)
        if right:
          construct_tree(right, root, ancestor)
        if parent == ancestor and len(str(ancestor)) == n:
          #print("OOO")
          #print(ancestor)
          #print(root.value, ancestor.value)
          trees.append(copy.deepcopy(ancestor))
          #print(trees)
          #ancestor = None
  construct_tree(ns, None, None)
  #print(trees)
  return trees 

for tree in generate_bst(3):
  print tree

for tree in generate_bst(5):
  print tree
