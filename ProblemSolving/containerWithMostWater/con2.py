class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Logic 1: Bruteforce with O(N)**2 --> works but time limit exceeded
        """
        maxi = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                h = min(height[i], height[j]) 
                l = j-i
                a = h*l
                if a > maxi:
                    maxi = a
                    
        return maxi
        """
        
        # Logic 2: 2 pointer method - all pass
        left = 0
        right = len(height)-1
        maxi = 0
        
        while left < right:
            h = min(height[left], height[right]) 
            l = right-left
            a = h*l
            if a > maxi:
                maxi = a
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            #print(height[left], height[right], a)
            
        return maxi
