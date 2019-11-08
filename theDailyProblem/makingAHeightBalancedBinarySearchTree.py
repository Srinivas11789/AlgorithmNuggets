"""
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    answer = str(self.value)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def create_height_balanced_bst(nums):
  # Fill this in.

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    answer = str(self.value)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def create_height_balanced_bst(nums):
  # To make it perfetly balanced with difference at most 1, break in the middle
  mid = len(nums)//2
  # Middle would be the current subtree root, set left and right
  left, right = None, None
  # Create left subtree and get the left subtree root
  if nums[:mid]:
    left = create_height_balanced_bst(nums[:mid])
  # Create right subtree and get the right subtree root
  if nums[mid+1:]:
    right = create_height_balanced_bst(nums[mid+1:])
  # Create the current subtree root node and set left and right
  n = Node(nums[mid])
  n.left = left
  n.right = right
  # Return current subtree node to recursively build
  return n
 
print create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
  
