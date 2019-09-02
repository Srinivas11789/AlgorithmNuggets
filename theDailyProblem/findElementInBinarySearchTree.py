"""
Given a binary tree, return all values given a certain height h.

Here's a starting point:

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print valuesAtHeight(a, 3)
# [4, 5, 7]
"""

result = []

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def traverse_and_find(node, height, current_height):
  global result
  #print(current_height, node)
  if current_height == height:
    result.append(node.value)
  if node.left:
    traverse_and_find(node.left, height, current_height+1)
  if node.right:
    traverse_and_find(node.right, height, current_height+1)
      

def valuesAtHeight(root, height):
  # Fill this in.
  traverse_and_find(root, height-1, 0) 

def main():
  global result
  a = Node(1)
  a.left = Node(2)
  a.right = Node(3)
  a.left.left = Node(4)
  a.left.right = Node(5)
  a.right.right = Node(7)
  valuesAtHeight(a, 3)
  print result

main()
