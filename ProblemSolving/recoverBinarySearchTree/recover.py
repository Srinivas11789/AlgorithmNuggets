# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        
        def inOrder(node ,ordering):
            
            if node.left:
                inOrder(node.left, ordering)
                
            if ordering:
                #print(node.val, ordering[-1].val, ordering)
                if node.val < ordering[-1].val:
                    for i in range(len(ordering)):
                        if i == 0 and ordering[i].val > node.val:
                            ordering[i].val, node.val = node.val, ordering[i].val
                        elif i == len(ordering)-1 and ordering[i].val > node.val:
                            ordering[i].val, node.val = node.val, ordering[i].val
                        elif ordering[i-1].val < node.val < ordering[i].val:
                            ordering[i].val, node.val = node.val, ordering[i].val 
            
            ordering += [node]
            
            if node.right:
                inOrder(node.right, ordering)
            
            return ordering
                
        order = inOrder(root, [])
