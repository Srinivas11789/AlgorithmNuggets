"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        
        # Recursive Method of finding depth
        def depth(node):
            
            # when a null node is reached from being recursive
            if not node:
                return 0
            else:
                # Node is not None and Node has children (Children check)
                # -- Go with maximum depth child as we progress
                if node.children:
                    return 1 + max([depth(child) for child in node.children])
                else:
                    # When the node has no children count its position
                    return 1
        
        # Root Node Null check
        if not root:
            return 0
        
        return depth(root)
        
        
        """
        # Iterative method -- 100% pass
        
        # Fill in each level (BFS mode) as a list of levels of a tree
        # -- The length of this (list of list/levels) will be the maximum depth
        
        # Null check
        if not root:
            return 0
        
        # Traverse levels helper
        stack = [[root]]
        
        # Levels list --- values at each level
        levels = []
        
        # Iterate until exhaust
        while stack:
            
            # current level to traverse in list
            current_level = stack.pop(0)
            
            # current levels values list
            levels.append([])
            
            # Next level list of children
            next_level = []
                
            # Exhaust current level list (all the current nodes)
            while current_level:
                # Remove node in each level (left to right)
                current_node = current_level.pop(0)
                
                # Update the current node values list (always the last in the list for that level)
                levels[-1].append(current_node.val)
                
                # Add all children to next level for traversing
                if current_node.children:
                    next_level.extend(current_node.children)
            
            # If there are nodes to traverse in the next level
            if next_level:
                stack.append(next_level)
                    
        #print levels
        
        # Depth
        return len(levels)
        """    
            
        """
        # Helpers/THoughts
            i, n = 0, len(prev_level)
            next_level = []
            while i < n:
                current = prev_level[i]
                if current.children:
                    stack.append([])
                    for child in current.children:
                        stack[-1].append(child)
                        next_level.append(child.val)
                i += 1
            stack.append(next_level)
        """
        
