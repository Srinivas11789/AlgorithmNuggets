# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Referring to https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106650/Python... - converting this logic to recursive --> Number the NODES in the tree
        
        # Logic 3: Do not recurse for None and do not consider None - 100 pass
        
        def levelOrderTraverse(node, height, num):
                
                if height not in self.levelOrder:
                    self.levelOrder[height] = [0, 0] # Just consider left and right pointer for boundaries

                if self.levelOrder[height][0] == 0:
                    self.levelOrder[height][0] = num
                else:
                    self.levelOrder[height][1] = num
                
                if self.levelOrder[height][0] > 0 and self.levelOrder[height][1] > 0:
                    self.max_width = max(self.max_width, self.levelOrder[height][1] - self.levelOrder[height][0] + 1)
                
                # Traverse by incrementing height
                if node.left:
                    levelOrderTraverse(node.left, height+1, num*2)
                    
                if node.right:
                    levelOrderTraverse(node.right, height+1, num*2+1)
        
        self.levelOrder = {}
        self.max_width = 0
        levelOrderTraverse(root, 1, 1)
        if self.max_width == 0 and root:
            self.max_width = 1
        print(self.levelOrder)
        return self.max_width
        
    
        # Logic 3: Iterative
        """
        stack = [(1, root)] # level and node
        width = 1
        while stack:
            width = max(width, stack[-1][0]-stack[0][0]+1) # Last node of current level and first node difference and + 1
            next_level = []
            for num, node in stack:
                if node.left:
                    next_level.append((num*2, node.left))
                if node.right:
                    next_level.append((num*2+1, node.right))
            #print(stack, next_level)
            stack = next_level
        return width
        """
            
        
        # Logic 2: Recursive Loop with max width calculation within loop - Still Time Limit Exceeded? ( Can you not recurse for None nodes and add something to improvise?)
        """
        def levelOrderTraverse(node, height):
            
            if height in self.levelOrder and height-1 in self.levelOrder and len(self.levelOrder[height]) >= 2*len(self.levelOrder[height-1]):
                return
            
            if node:
                # If there is a node then create height
                # Add height to dictionary 
                if height not in self.levelOrder:
                    self.levelOrder[height] = None
                    
                # Update height - We can calculcate the length here as we know for sure this is a number that could represent a boundary
                #self.levelOrder[height]["nodes"].append(str(node.val))
                if not self.levelOrder[height]:
                    self.levelOrder[height] = [str(node.val)]
                else:
                    self.levelOrder[height].append(str(node.val))
                
                self.max_width = max(self.max_width, len(self.levelOrder[height]))
                
                # Update max_width as we add a number that represents a boundary
                #if self.levelOrder[height]["nodes"]["left"] == None:
                #     self.levelOrder[height]["nodes"]["left"] = 
                # self.levelOrder[height]["nodes"]["right"] = len(self.levelOrder[height]["nodes"]-1)
                # self.max_width = max(self.max_width, len(self.levelOrder[height]["nodes"][self.levelOrder[height]["left"]:self.levelOrder[height]["right"]]))
                
                # Traverse by incrementing height
                levelOrderTraverse(node.left, height+1)
                levelOrderTraverse(node.right, height+1)
            elif height in self.levelOrder and height-1 in self.levelOrder and len(self.levelOrder[height]) < 2*len(self.levelOrder[height-1]):
                # Update NULL - lets use empty space count only inbetween nulls - and only if they have a left boundary
                if height in self.levelOrder and len(self.levelOrder[height]) < 2*len(self.levelOrder[height-1]):
                    self.levelOrder[height].append(None)
                    if height+1 in self.levelOrder and self.levelOrder[height+1] != None and len(self.levelOrder[height+1]) < 2*len(self.levelOrder[height]):
                        levelOrderTraverse(None, height+1)
                        levelOrderTraverse(None, height+1)
        
        self.levelOrder = {}
        self.max_width = 0
        levelOrderTraverse(root, 1)
        return self.max_width
    """
        
        # Logic 1: Perform a Level Order Search for each height and then calculate length - time limit exceeded ( can you fit the length calculation during the recurse itself? )
        """
        def levelOrderTraverse(node, height):
            
            # Add height to dictionary 
            if height not in self.levelOrder:
                self.levelOrder[height] = []
            
            if node:
                # Update height
                self.levelOrder[height].append(str(node.val))

                # Traverse by incrementing height
                levelOrderTraverse(node.left, height+1)
                levelOrderTraverse(node.right, height+1)
            else:
                # Update NULL - lets use empty space count only inbetween nulls
                self.levelOrder[height].append(None)
                if height+1 in self.levelOrder:
                    levelOrderTraverse(None, height+1)
                    levelOrderTraverse(None, height+1)
        
        self.levelOrder = {}
        levelOrderTraverse(root, 1)
        print(self.levelOrder)
        max_width = 0
        for level in self.levelOrder.keys():
            #max_width = max(len("".join(self.levelOrder[level]).strip()), max_width)
            left, right = 0, len(self.levelOrder[level])-1
            while left < right and self.levelOrder[level][left] == None:
                left += 1
            while right > left and self.levelOrder[level][right] == None:
                right -= 1
            print(self.levelOrder[level], left, right)
            max_width = max(max_width, len(self.levelOrder[level][left:right+1]))
        return max_width
        """
