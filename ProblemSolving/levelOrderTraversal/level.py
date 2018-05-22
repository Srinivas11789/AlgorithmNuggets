# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        result = []
        nodes = []
        nodes.append(root)
        
        while 1:
            
            n = len(nodes)
            
            if n == 0:
                break
            
            result.append([])
        
            while n > 0:
                """       
                if n == 0:
                    result.append([])
                    n = len(nodes)
                else:
                    result[-1].append(node.val)
                """
                node = nodes.pop(0)
                print node.val,
                result[-1].append(node.val)
            
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            
                n -= 1
            
            #result.append([nodes])
            #nodes = []
            #print "\n"
            
        return result
        
	"""
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        nodes = []
        nodes.append(root)
        n = len(nodes)
        
        while len(nodes) > 0:
        
            node = nodes.pop(0)
            
            n -= 1
            print node.val,
            
            if n == 0:
                if nodes:
                    result.append([num.value for num in nodes])
                n = len(nodes)
    
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
                
            n = len(nodes)
            
        return result
    
        """
        def search(root):
            
            nodes = []
            children = []
            nodes.append(root)
            
            while len(nodes) > 0:
                                 
                #for node in nodes:
                #    result[-1].append(node.val)
                
                node = nodes.pop(0)
                print node.val
                
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            
           # return result
           """
                
            
        """
            # Iterate through each level and make them a list and save to a bigger list
            if not root:
                return
            
            if len(result) == 1:
                nodes = []
                
            search(root.left)
            search(root.right)
            
            result.append(nodes)
            nodes = []
            
            if root:
                if root.left:
                    nodes.append(root.left.val)
                if root.right:
                    nodes.append(root.right.val)
                    
        """
            
        """
            nodes = []
            
            nodes.append([root.val])
                
            while root.left or root.right:
            
                if root.left:
                    nodes.append(root.left.val)
                if root.right:
                    nodes.append(root.right.val)
                    
                result.append(nodes)
            return result
            """
        """   
        # Driver
        result = []
        if root:
            search(root)

        return result
        """
    
