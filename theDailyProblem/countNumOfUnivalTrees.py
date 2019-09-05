"""
A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)

Here's a starting point:

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
  # Fill this in.

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print count_unival_subtrees(a)
# 5
"""

count = 0

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(node):
  global count
  if not node:
    return [] 
  lsubtree = []
  rsubtree = []
  if node.left:
    lsubtree += count_unival_subtrees(node.left)
  if node.right:
    rsubtree += count_unival_subtrees(node.right)
  subtree = [node.val] + lsubtree + rsubtree
  if len(set(subtree)) == 1:
    count += 1
  return subtree

def main():
  global count
  a = Node(0)
  a.left = Node(1)
  a.right = Node(0)
  a.right.left = Node(1)
  a.right.right = Node(0)
  a.right.left.left = Node(1)
  a.right.left.right = Node(1)
  count_unival_subtrees(a)
  print(count)

main()
