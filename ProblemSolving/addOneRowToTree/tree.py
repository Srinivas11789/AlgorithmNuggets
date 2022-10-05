# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def insertLevel(node, curLvl):

            if curLvl+1 != depth:
                if node.left:
                    insertLevel(node.left, curLvl+1)
                if node.right:
                    insertLevel(node.right, curLvl+1)
                return 

            print(curLvl, node.val)

            if node.left:
                tmp = node.left
                node.left = TreeNode(val)
                node.left.left = tmp
            else:
                node.left = TreeNode(val)

            if node.right:
                tmp = node.right
                node.right = TreeNode(val)
                node.right.right = tmp
            else:
                node.right = TreeNode(val)

        curLvl = 1
        if curLvl == depth:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        insertLevel(root, curLvl)
        return root
