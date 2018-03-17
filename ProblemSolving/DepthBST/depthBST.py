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

    def getHeight(self,root):
        #Write your code here
        #  Misses the path route over the middle 
        """
        height_right = 0
        height_left = 0
        right = root
        left = root
        while right.right:
            right = right.right
            height_right += 1
        while left.left:
            left = left.left
            height_left += 1
        if height_left > height_right:
            return height_left
        else:
            return height_right
        ###
        """
        ### Leaf Logic would be --> if both left.left and left.right are None
        # Recursive is the best solution
        """
        if root is None:
            return -1
        else:
            #print root.data
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            #print left_height, right_height
            if left_height > right_height:
                return left_height+1
            else:
                return right_height+1
        """
        
        # Recursive + One Line SOlution
        if root is None:
            return -1
        else:
            return 1+max(self.getHeight(root.left),self.getHeight(root.right))

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height       
