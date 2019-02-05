# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        # Gathering some known properties and findings:
        # PreOrder 
        # * has root at the beginning [Root, Left, Right] 
        # * Ends with the right most node of the tree
        # PostOrder 
        # * has root at the end [Left, Right, Root] 
        # * Starts with the left most node of the tree
        
        # Root
        root = TreeNode(pre.pop(0))
        head = post.pop(-1)
        
        # To help us traverse through the tree
        stack = [root]
        
        
        # The learnings until now, appending to the list above:
        # * Pre ==> Root, L, R ==> If we find a root, then the subsequent nodes are left and right
        # * Post ==> L, R, Root ==> By ensuring we hit a root we can be confident that the all nodes of that subtree have been exercised
 	# * This <https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)> seems to be an elegant approach of the same understanding. Using as reference...      

        pnode = 0
        
        for node in pre:
        
            current_node = TreeNode(node)
            
            # Ensure, if the root is reached in post order to confirm the subtree has been exercised
            while stack[-1].val == post[pnode]:
                stack.pop()
                pnode += 1
            
            # If there is no left, add left
            if not stack[-1].left:
                stack[-1].left = current_node
            elif not stack[-1].right:
                stack[-1].right= current_node
            
            # Each node can be a root in pre, append to stack to traverse
            stack.append(current_node)
        
        return root
        
        """
        # We should leverage some logic to iteratively perform the node addition rather than following the steps literally
        # * This works by literally following the logic, more better of the same implementation above...
        
        # pre and post ==> Both are equal number of nodes as guaranteed the answer exists
        while pre and post:
            
            # First, reach the left mode node
            left_most_node = post.pop(0)
            while pre[0] != left_most_node:
                root.left = TreeNode(pre.pop(0))
                root = root.left
                stack.append(root)
            # Add the left most node
            root.left = TreeNode(pre.pop(0))
            
            # Second, traverse back up to the root adding the right nodes
            # * where to stop ==> The left subtree ends when upper most left child is reached...
            while stack and post[0] != stack[0].val:
                parent = stack.pop(-1)
                if post[0] == parent.val:
                    post.pop(0)
                elif post[0] == parent.left.val:
                    post.pop(0)
                else:
                    parent.right = post.pop(0)
            
            # Upper most left node
            if stack:
                post.pop(0)
            # reset root
            root = head
            # Left subtree is done!
            
            # Right subtree
            root.right = post.pop(-1)
        """
                
                
            
            
            
            
            
            
            

            
            
            
