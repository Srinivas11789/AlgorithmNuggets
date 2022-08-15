# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Logic: Calculate including and not including parent separately
        
        memoSteal = {}
        memoNoSteal = {}
        
        #@cache # indirect memo --> 100 pass 68% faster
        def recurse(house, parent_stolen):
            
            if not house:
                return 0
            
            if parent_stolen: # then children is not stolen, so skip to next
                if house in memoNoSteal:
                    return memoNoSteal[house]
                
                max_stolen_skipped = 0
                max_stolen_skipped += recurse(house.left, False)
                max_stolen_skipped += recurse(house.right, False)
                memoNoSteal[house] = max_stolen_skipped
                
                return memoNoSteal[house]
            else: # parent is not stole, so we have choice to steal or not steal children --> calc both to check max
                if house in memoSteal:
                    return memoSteal[house]

                max_stolen_robd = house.val
                max_stolen_robd += recurse(house.left, True)
                max_stolen_robd += recurse(house.right, True) 
                
                max_stolen_skipped = 0
                max_stolen_skipped += recurse(house.left, False)
                max_stolen_skipped += recurse(house.right, False)
                
                memoSteal[house] = max(max_stolen_robd, max_stolen_skipped)
                    
                return memoSteal[house]
            
        return recurse(root, False)       
        
        # Logic to decompose problem into adjacent level housing and solving wont work --> 2,1,3,null,4 adds usecase with not directly linked subtree selections
        """
        
        # 1. level order traverse to get house values by levels
        # 2. perform adjacent house method
        self.levels = []
        
        def traverse(node, level):
            
            if level >= len(self.levels):
                self.levels.append(0)
                
            self.levels[level] += node.val
            
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
            
        self.memo = {}
        
        def robN(level):
            
            if level >= len(self.levels):
                return 0
            
            if level in self.memo:
                return self.memo[level]
            
            self.memo[level] = max(self.levels[level]+robN(level+2), robN(level+1))
            return self.memo[level]
        
        traverse(root, 0)
        robN(0)
        
        print(self.memo, self.levels)
        return self.memo[0]
        """
        
