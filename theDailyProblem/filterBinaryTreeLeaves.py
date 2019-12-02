"""
Given a binary tree and an integer k, filter the binary tree such that its leaves don't contain the value k. Here are the rules:

- If a leaf node has a value of k, remove it.
- If a parent node has a value of k, and all of its children are removed, remove it.

Here's an example and some starter code:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"

def filter(tree, k):
  # Fill this in.

#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)

print(filter(n1, 1))
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

  def __repr__(self):
      #if self.left:
      #  self.left.__repr__()
      #print(self.val)
      #if self.right:
      #  self.right.__repr__()
      return "value: { " + str(self.val) + " }, left: ({" +  str(self.left.__repr__()) + "}), right: ({" + str(self.right.__repr__()) + "})"

def filter(node, k, parent, orient):
 
    # Recurse for each child -> left and right
    if node.left:
      filter(node.left, k, node, "left")
    if node.right:
      filter(node.right, k, node, "right")

    # filter the nodes if value is `k` and no children
    if node.val == k and not node.left and not node.right and parent:
      if orient == "left":
        parent.left = None
      if orient == "right":
        parent.right = None
  
    # If root is k and all subtree nodes is k
    if not parent and not node.left and not node.right:
      return Node("")
    else:
      return node

#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)

print(filter(n1, 1, None, None))
