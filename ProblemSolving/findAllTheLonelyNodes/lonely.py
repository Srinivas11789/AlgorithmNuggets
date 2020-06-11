# Logic 1: Traverse tree + find parent with one node: 50% faster

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
    
        def traverseTree(node):
            if not node:
                return
            children = []
            if node.left:
                children.append(node.left.val)
                traverseTree(node.left)
            if node.right:
                children.append(node.right.val)
                traverseTree(node.right)
            if len(children) == 1:
                self.lonely.append(children[0])
    
    
        self.lonely = []
        traverseTree(root)
        return self.lonely
        
        
