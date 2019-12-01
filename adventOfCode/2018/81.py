# Arrangement:
# * We provide our own naming
# * Each node: 1st num of children
# *            2nd metadata size

# Part 1 --> sum of all the metadata

### Rock Solid Logic: Contruct a Nary Tree and work out from there

class node:
    def __init__(self, children_size, metadata_size):
        self.no_of_children = children_size
        self.metadata_size = metadata_size
        self.children = []
        self.parent = None
        self.metadata = ""
        # Part 2
        self.value = 0

fullStack = []
             
def construct_a_tree(data):
    n = len(data)
    i = 0
    root = None
    while i < n:
        
        # Safe?
        #if fullStack and fullStack[-1].children == 0 and root == fullStack[-1]:
        #   fullStack[-1].metadata += "".join(data[i:i+fullStack[-1].metadata_size])
        #   i += fullStack[-1].metadata_size
        #   break
        
        #debug
        #print i
        #if fullStack:
        #    print fullStack[-1].metadata_size, fullStack[-1].no_of_children, i 
        
        current = node(int(data[i]), int(data[i+1]))
        if not root: 
	   root = current
        if current.no_of_children > 0:
            fullStack.append(current)
            #current.no_of_children -= 1
            i += 2
        else:
            current.metadata = data[i+2:i+current.metadata_size+2]
            i += 2+current.metadata_size
            fullStack[-1].children.append(current)
            fullStack[-1].no_of_children -= 1  
            current.parent = fullStack[-1]
            while fullStack and fullStack[-1].no_of_children == 0:
               fullStack[-1].metadata = data[i:i+fullStack[-1].metadata_size]
               i += fullStack[-1].metadata_size
               next = fullStack.pop()
               if fullStack:
                   fullStack[-1].children.append(next)
                   fullStack[-1].no_of_children -= 1
        if i > n:
               break
    
    #print root.metadata, root.children
    return root

# Part 1 question ==> Metadata sum of all nodes
# Recursively traverse the tree for metadata sum
def calc_metadata(node, metadata_sum):
    #print node.metadata, metadata_sum     

    metadata_sum = sum([int(data) for data in node.metadata])

    for child in node.children:
        metadata_sum += calc_metadata(child, metadata_sum)

    return metadata_sum

# Part 2 question ==> Value of the root node
def root_value(node):

    # Logic to calculate the value
    if len(node.children) == 0:
       node.value = sum([int(data) for data in node.metadata])
    else:
       for md in list(set(node.metadata)):
           if int(md)-1 < len(node.children):
              node.value += root_value(node.children[int(md)-1]) * (node.metadata.count(md))
           else:
              # metadata greater than children list index
              node.value += 0

    return node.value
  
def main():
    # Fetch input from url
    import requests, sys
    # Sent the cookie set through the environment variable to get this
    #input = requests.get("https://adventofcode.com/2018/day/8/input")

    # Hard Coded inputs
    input = open("81.input","r").read()
    input = input.split("\n")[0].split(" ")
    root = construct_a_tree(input)
    print "Day 8: Part 1 answer is --> " + str(calc_metadata(root, 0))
    print "Day 8: Part 2 answer is --> " + str(root_value(root))

main()

# Logic 1: Construct a dictionary
"""
def traverse(data):
    stack = {}
    n = len(data)
    i = 0
    while i < n:
        element = stack[]
        if element.children == 0:
                element.metadata += data[i+1:i+1+n]
        stack.append(element)

# Logic 2: Stack Method
# * The metadata of A is after all the children metadata are filled. When there is heavy nesting a tree  mthod would require a depth first traversal either way to add the children and fill in the metadata values.
# Backward traversal is a little tough for tree. Going with stack logic
class node:
    def __init__(children, metadata_size):
        self.children = children
        self.metadata = metadata_size
        self.metadata = ""

def traverse(data):
    stack = []
    n = len(data)
    i = 0
    while i < n:
        element = node(data[i], data[i+1])
        if element.children == 0:
                element.metadata += data[i+1:i+1+n]
        stack.append(element)

# Logic 3: Construct a tree
class node:
    def __init__(self, children, metadata_size, index, parent):
        # Integer num of children
        self.children = children
        # Integer size of metadata
        self.metadata = metadata_size
        # Metadata string
        self.md = ""
    # Store index in the array
        self.index = index
        # Children node in a list
        self.childs = []
        # Parent details
        self.parent = parent

# Possible recursion function to iterate through the tree
def create_tree(data, parent, next):
    #i = current_index

    #if parent.children == 0:
    #   parent.md += "".join(data[i+1:i+parent.metadata+1])
    #   return parent, i+parent.metadata

    while parent.children:
        #curr_child = node(int(data[next+1]), int(data[next+2]), next+1)
        #tree_for_child, next = create_tree(data, curr_child, next+1)
        curr_child = node(int(data[0]), int(data[1]), 1)
        tree_for_child, next = create_tree(data[2:], curr_child, 1)
        parent.childs.append(tree_for_child)
        parent.children -= 1

    if parent.children == 0:
       #if next+parent.metadata+1 > len(data):
       #   parent.md += "".join(data[next+3:])
       #else:
       #   parent.md += "".join(data[next+3:next+parent.metadata+1])
       parent.md += "".join(data[:parent.metadata])
       print parent.metadata, parent.md
       return parent, next+parent.metadata
    
    #return parent

def traverse(data):
    root = node(int(data[0]), int(data[1]), 0, None)
    create_tree(data[2:], root, 1)
    return root.md, root.childs[0].md

def traverse(data):
    n = len(data)
    prev_node = None
    full_stack = []
    while i < n:
        current_node = node(int(data[i]), int(data[i+1]), i, prev_node)
        prev_node = current_node
        full_stack.append()
"""
