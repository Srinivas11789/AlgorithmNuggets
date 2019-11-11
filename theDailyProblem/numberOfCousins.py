"""
Given a binary tree and a given node value, return all of the node's cousins. Two nodes are considered cousins if they are on the same level of the tree with different parents. You can assume that all nodes will have their own unique value.

Here's some starter code:

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print Solution().list_cousins(root, 5)
# [4, 6]
"""

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    levels = {}
    self.current_node_level = None
    def traverse(node, val, level):
        if not node:
          return
        if level not in levels:
          levels[level] = []
        #print(node.val ==  val)
        if node.val == val:
          self.current_node_level = level
        else:
          levels[level].append(node.val)
        traverse(node.left, val, level+1)
        traverse(node.right, val, level+1)
         
    traverse(tree, val, 0)
    #print(levels, self.current_node_level)
    return levels[self.current_node_level]

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print Solution().list_cousins(root, 5)
# [4, 6]
