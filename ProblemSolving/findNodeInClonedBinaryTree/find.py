# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
        # Brainstorm:
        # * Both the trees are copies so their structure remains the same, iterate or traverse together?
        # * I think they mean deep copy (not shallow copy) here and we need to find the reference of the exact node even when there are repeated values
        # * By nature bst has distinct keys --> Can the logic also support when repeated values occur?
        #   - Means we need to check if the parents and childrens are the same or subtree at that node is same
        
        # Logic 1: Traverse 2 trees - 100 pass 17.6%
        def traverseBothTree(original, cloned, target, result):
            print(self.result)
            # Check node not null
            if not original:
                return None

            # Exit criteria
            if original.val == cloned.val == target.val:
                self.result = cloned

            # Traverse the tree together
            if original.left and not self.result:
                self.getTargetCopy(original.left, cloned.left, target)

            if original.right and not self.result:
                self.getTargetCopy(original.right, cloned.right, target)
        
        self.result = None
        traverseBothTree(original, cloned, target, self.result)
        print(self.result)
        return self.result
    
        # Logic 2: Repeated values would be allowed?
        
        
