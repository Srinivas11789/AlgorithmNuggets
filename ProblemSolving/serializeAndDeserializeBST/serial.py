# Pending...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Logic:
# * Given a root,Lets use any one traversal technique (pre, post or in order) or level order and obtain a string (or any technique to traverse)
# * Given a string, Lets reverse the corresponding order we select and reconstruct the tree
# * Remember we do it state less so we dont store any variables

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def pre_order_traverse(node, encode):
            
            if not node:
                return
        
            if node.left and node.right:
                encode += "/"+ str(node.val) +  "L" + str(node.left.val) +  "R" + str(node.right.val)
            elif node.left:
                encode += "/"+ str(node.val) + "L" + str(node.left.val)
            elif node.right:
                encode += "/"+ str(node.val) + "R" + str(node.right.val)
            elif node:
                encode += "/"+str(node.val) 
                
            pre_order_traverse(node.left, encode)
            pre_order_traverse(node.right, encode)
            
            return encode
            
        return pre_order_traverse(root, "")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def reverse_traversal_to_bst(node, sequence, root):
            
            if sequence and node == "":
                subtree = list(sequence.pop(0))
                root = node = TreeNode(int(subtree.pop(0)))
                if subtree and subtree[0] == "L":
                    subtree.pop(0)
                    node.left = TreeNode(int(subtree.pop(0)))
                if subtree and subtree[0] == "R":
                    subtree.pop(0)
                    node.right= TreeNode(int(subtree.pop(0)))
            
            elif sequence and node.val == sequence[0]:
                subtree = list(sequence.pop(0))
                subtree.pop(0)
                if subtree and subtree[0] == "L":
                    subtree.pop(0)
                    node.left = TreeNode(int(subtree.pop(0)))
                if subtree and subtree[0] == "R":
                    subtree.pop(0)
                    node.right= TreeNode(int(subtree.pop(0)))
            
            if node.left:
                reverse_traversal_to_bst(node.left, sequence, root)
            if node.right:
                reverse_traversal_to_bst(node.right, sequence, root)
            
            return root
            
        if not data:
            return []
        print data
        return reverse_traversal_to_bst("", data.split("/")[1:], "")
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# print codec.serialize(root)
# codec.deserialize(codec.serialize(root))
