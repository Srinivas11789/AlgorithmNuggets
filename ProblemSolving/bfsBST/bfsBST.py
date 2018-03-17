import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    
    ### Base Logic is take every node ---> push into a queue ---> Print and delete the node from the queue
    ### --> Finally add the left and right to the end of the queue
    def levelOrder(self,root):
        
        # Root None criterion
        if root is None:
            return
        
        # List of all the nodes at that particular level
        nodes = []
        
        # Root appended initially
        nodes.append(root)
        
        # Append all nodes at each level 
        while len(nodes) > 0:
            
            # Stdout node at the current level one by one
            print nodes[0].data,
            
            # Delete the node once the node is output
            node = nodes.pop(0)
            
            #Append the left and right for each node visited
            if node.left is not None:
                nodes.append(node.left)
                
            if node.right is not None:
                nodes.append(node.right)
            
            
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
