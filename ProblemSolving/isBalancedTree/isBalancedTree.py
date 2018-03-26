# Binary Search Tree

#### Class Node to hold the structure of each node

class node:

      def __init__(self, value, left, right):
	self.value = value
	self.left = left
	self.right = right


def height(node):
    if node is None:
       return -1
    else:
       return max(height(node.left),height(node.right))+1

def balancedSubtree(root):
    if root == None:
       return 0;
    left = balancedSubtree(root.left)
    right = balancedSubtree(root.right)
    if left<0 or right<0 or abs(left-right)>1:
       return -1
    return max(left,right)+1


def main():
    root = node(1,None,None)
    root.left = node(2,None,None)
    root.right = node(3,None,None)
    print root.value
    print root.left
    print height(root)
    print balancedSubtree(root)

main()
