# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # PreOrder Search BST as soon as you get root
        self.result = []
        def preorder(node):
            if node:
                preorder(node.left)
                self.result.append(node.val)
                preorder(node.right)
        preorder(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.result:
            return self.result.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.result:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
