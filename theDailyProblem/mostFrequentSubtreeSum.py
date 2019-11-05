"""
Given a binary tree, find the most frequent subtree sum.

Example:

   3
  / \
 1   -3

The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

If there is a tie between the most frequent sum, you can return any one of them.

Here's some starter code for the problem:

class Node():
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def most_freq_subtree_sum(root):
  # fill this in.

root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1
"""

class Node():
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def traverse(node):
    global maxi
    if not node:
        return 0
    current_sum = node.val + traverse(node.left) + traverse(node.right)
    if current_sum not in sums:
        sums[current_sum] = 0
    sums[current_sum] += 1
    if sums[current_sum] > maxi:
        maxi = sums[current_sum]
    return current_sum

sums = {}
maxi = 0
root = Node(3, Node(1), Node(-3))
traverse(root)
print([k for k,v in sums.items() if v == maxi])
# 1

