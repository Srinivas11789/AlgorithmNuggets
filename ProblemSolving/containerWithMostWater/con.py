class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        """
        # Logic 1 
        # Lets start with maximizing x (i2-i1) and combine with 2 pointer method
        n = len(height)
        left = 0
        right = n-1
        initial_x = right - left
        """
        
        """
        # Attempt 1 
        # Logic 2 - Dictionary method (Time limit exceeded) -- optimize
        # Select maximum Ys with maximum Xs, decrease Ys as we progress and find one with maximum X
        
        # Create a dictionary of all the positions (Xs) and veritcal lengths (Ys)
        pos = {}
        n = len(height)
        for i in range(n):
            while height[i]:
                if height[i] not in pos:
                    pos[height[i]] = []
                pos[height[i]].append(i)
                height[i] -= 1
        
        # Last - first is the highest x, calculate all the x*y in the dictionary
        maxi = 0
        for key,val in pos.items():
            if len(val) >= 2 and (val[-1]-val[0]) * key > maxi:
                maxi = (val[-1]-val[0]) * key
        return maxi
        """
        
        # Attempt 2 
        # Logic 2 - Attempt 1 (Time limit exceeded) -- optimize?
        # Select maxi * i, calculate only until maxi = i so that a maximum occurrence is possible
        # Increases time further to add this logic???
        
        # Attempt 3 - Going with logic 1
        # Going to the Attempt 1 with the 2 pointer method. We need to converge to the center as we progress so that we can track the distance(x) and the corresponding max length as we progress
        n = len(height)
        
        # 2 pointer method
        left = 0
        right = n-1
        
        # initial maximum
        maxi = 0
        
        # Iterate backwards so we keep track of maximum 'x' as we move through
        for i in range(n-1, -1, -1):
            # Keep track of maximum as we progress through the array backwards maintaining max 'x'
            # for any right, when left is less, it can match all right (5 vs 8 ==> 1,8 2,8 3,8 ... 5,8)
            if height[left] < height[right]:
                maxi = max(height[left] * i, maxi)
                left += 1
            else:
                # Similarly for right
                maxi = max(height[right] * i, maxi)
                right -= 1
        return maxi
                
            
        
    
        
    
    
        
            
            
        
            
        
        
