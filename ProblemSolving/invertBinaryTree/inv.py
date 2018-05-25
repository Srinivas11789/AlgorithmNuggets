# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # 100 pass logics
        # Aim is to invert the left and right nodes
        
        """
        # Using Recursion
        def invertTree(node):
            
            if not node:
                return None
            else:
                node.left, node.right = invertTree(node.right), invertTree(node.left)
                return node
        
        return invertTree(root)
        """
    
        # Using Iteration 
        if not root:
            return []
        
        # Use a stack here as we want to invert the tree taking every right node first and then the left node
        nodes = [root] # Initially with root
        
        
        # Traverse the stack --> take every node --> interchange the left and the right node --> append left and right to the stack 
        while len(nodes) > 0:
            node = nodes.pop()
            
            # If node is not null as sometimes null nodes are stored as well
            if node:
                node.left, node.right = node.right, node.left
                nodes.extend([node.left, node.right])
        
        return root
        
        """
        # Did not work quite -- long approach
        # Hacky Solution - Do a level order traversal and reverse all the levels except the root
        
        if not root:
            return []
    
        # To hold all the nodes as a queue while we traverse - initially contains the root
        nodes = [root]
        
        # To hold the result with all the levels
        result = []

        while len(nodes) > 0:
            
            # Level append
            result.append([])
            n = len(nodes)
            
            while n > 0:
                
                # Queue operation to traverse as we move
                select = nodes.pop(0)
                
                if select:
                    result[-1].append(select.val)
                    if select.left:
                        if not select.right:
                            nodes.append(select.left)
                            nodes.append(None)
                        else:
                            nodes.append(select.left)
                    if select.right:
                        if not select.left:
                            nodes.append(None)
                            nodes.append(select.right)
                        else:
                            nodes.append(select.right)
                else:
                    result[-1].append(select)
                
                n -= 1
        
        print result
        answer = []
        for level in result:
            answer.extend(level[::-1])
        
        while answer[len(answer)-1] == None:
                answer.pop()
            
        return answer
        """ 
                
        
