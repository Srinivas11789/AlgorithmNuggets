# Breath First Search or Level Order Search
"""
* Level order search is when you go breath wise traversing each element of the binary search tree 
There are two possible outcomes expected,

1. Make a levelOrderTraversal and print the node values of each row you traverse level wise or row wise
Example:
	a
       / \
      b   c
Should be output as [[a], [b,c]] or a\n b,c\n
The first one required 2 loops to iterate through each level and another loop to traverse through each nodes in that level

2. A more general approach of traversing the tree through breath first search by only listing all the nodes and not based on their levels
Example:
        a
       / \
      b   c
Should be output as [a,b,c] or a,b,c
In this case only one loop is required to traverse through the list all the nodes
"""

# Traverse based on levels --> 

1.
def levelOrderI(root):

        # Root null check
        if not root:
            return []
        
	# Reference as we traverse the array
        nodes = [root]

        # Result holding list
        result = []
        
	# Loop for each level as we move through - <avoid using infinite loops>
        while len(nodes) > 0:
     
            # number of nodes to traverse in the current level
            n = len(nodes)

            # Append the level list 
            result.append([])
  
            # Traverse only through the nodes in that level by queue operation = pop(0)
            while n > 0:
                current = nodes.pop(0)
                # Append only the specific level
                result[-1].append(current.val)
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)
                n -=1
        print result


# General level order traversal 

def levelOrder2(root):
       
        if not root:
            return []
        
        nodes = [root]
        result = []
        
	# Single loop to traverse over all the nodes
        while len(nodes) > 0:
            current = nodes.pop(0)
            result.append(current.val)
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)
        print result

