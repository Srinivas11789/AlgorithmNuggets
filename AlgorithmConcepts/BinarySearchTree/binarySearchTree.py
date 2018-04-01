# Nodes Structure

class Node:
	
	def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

	def print_node(self):
            print(self.value, self.right, self.left)


# Insert Node

# Logic: Traverse through the tree based on bst logic (left: lower, right: higher) and insert corresponding node

def insert(root, value):
    
      if value < root.value:
         if root.left == None:
            root.left = Node(value)
         else:
            insert(root.left, value)
      else:
         if root.right == None:
            root.right = Node(value)
         else:
            insert(root.right, value)
 

# Delete Node

# Find a node - search

def find(root, value):
    
    if root.value == value:
       return 1
    if value < root.value and root.left is not None:
       find(root.left, value)
    else:
       if root.right is not None:
       	find(root.right, value)
    return 0

# isBinary Search Tree

def isBST(root):
    
    if root.value > root.left.value and root.value < root.right.value:
       return 1
    else:
       return 0

    if root.left != None:
       isBST(root.left)
    if root.right != None:
       isBST(root.right)

# Breath first search

# Depth first search

# is a Balanced binary search tree

# Height of a binary search tree

# Maximum subtree 

# Maximum balanced subtree

# Print a binary search tree

def printBST(root):
    if root.value == None:
       return
    print(str(root.value))
    if root.left is not None:
       #print("\t\t"+"//")
       printBST(root.left,)
    if root.right is not None:
       #print("\t\t"+"\\")
       printBST(root.right,)
          

# Main Driver Program

def main():
    root = Node(3)
    insert(root,4)
    insert(root,2)
    insert(root,1)
    insert(root,3)
    printBST(root)	
    print find(root,3)
    print find(root,5)
    print isBST(root)
main()
