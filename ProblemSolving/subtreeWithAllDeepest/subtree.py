# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Height of the tree calculation
        def height_of_the_tree(node):
            if not node:
                return 0
            else:
                return 1 + max(height_of_the_tree(node.left), height_of_the_tree(node.right))
        
        # Traverse the tree
        # Rethink:
        # * You are required to find the subtree (root of subtree) which has the max height nodes
        # -- This can be true only if the farthest nodes are reachable from the same node (I knew about this but was more prone to get the list of nodes rather than just the root, also tried to solve it recursively which took a long time)
        # -- Else, find the subtree whose height is the largest either left or right
        # * Took inspiration from https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/226585/simple-and-faster-python.Hit-it-if-you-like.
        while root:
            left = height_of_the_tree(root.left) 
            right = height_of_the_tree(root.right)
            
            if left == right:
                return root
            elif left > right:
                root = root.left
            else:
                root = root.right
        
        
        """
        # This idea doesnt work,
        # * The part which I think I missed was,
        # * Sometimes the common deepest nodes exist wide from each other that the common parent resides way above them in a tree (Solve this!)
        self.deepest = 0
        self.deepest_subtree = []
        
        def traverse_deepest(node, past_depth, parent):
            
            if node.left:
                traverse_deepest(node.left, past_depth+1, node)
            
            if node.right:
                traverse_deepest(node.right, past_depth+1, node)
            
            if past_depth > self.deepest:
                self.deepest = past_depth
                self.deepest_subtree = [parent.val, node.val]
            elif past_depth == self.deepest and parent.val == self.deepest_subtree:
                self.deepest_subtree.append(node.val)
            elif past_depth == self.deepest and parent.val != self.deepest_subtree:
                
        
        traverse_deepest(root, 0, 0)
        if len(self.deepest_subtree) == 2:
            self.deepest_subtree = self.deepest_subtree[1:]
        return self.deepest_subtree
        """
        
        """
        # Previous Irrelevant Brainstorming...
        self.deepest = 0
        self.deepest_subtree = []
        
        def depth_of_node(node, depth, parent):
            
            if not node:
                return 0       
            else:
                depth += max(depth_of_node(node.left, depth+1, node), depth_of_node(node.right, depth+1, node))
                print node.val, depth
                if not node.left and not node.right:
                    if depth >= self.deepest:
                        self.deepest_subtree = []
                        self.deppest = depth
                        self.deepest_subtree.append(node.val)
                        if parent.val not in self.deepest_subtree:
                            self.deepest_subtree.append(parent.val)
                return depth
        
        depth = depth_of_node(root, 0, root)
        print depth, self.deepest, self.deepest_subtree
        
        #def traverse(node):
        #    
        #    if not node:
        ##        return 0
        #    else:
                
        #if depth > self.deepest:
        #    self.deepest = depth
        #    self.deepest_subtree = [node.val, node.left.val, node.right.val]
        """
        
        
