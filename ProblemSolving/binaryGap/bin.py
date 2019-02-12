class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # Brute force method, naive iteration to find consecutive ones
        # * One loop for 1st one
        # * Second loop for 2nd one
        # * We already traverse digits in between, so move forward the index to the second one for the next loop....
        binary = bin(N)
        #print binary
        
        # Control vars
        n = len(binary)
        maxi = 0
        
        # iteration until finding the 1st one
        i = 0
        while i < n:
            if binary[i] == "1":
                # iteration for 2nd one
                j = i+1
                while j < n:
                    # Break as soon as consecutive one is found and adjust index to the consecutive one
                    if binary[j] == "1":
                        maxi = max(maxi, j-i)
                        i = j-1 # Once you break after finding consecutive, while loop iterates i += 1, to handle that negate i before breaking
                        break
                    j += 1
            i += 1
                        
        return maxi                       
        
        """
        # Logic:
        # * Convert number to a usable form of binary
        # * Only the max is required, use 2 pointer method to return on first match --> does not work when consecutive ones need to be worked on.
        binary = str(bin(N))[2:]
    
        left = 0
        right = len(binary)-1
        
        while left <= right:
            if binary[left] == "1":
                break
            left += 1
        
        while right >= left:
            if binary[right] == "1":
                break
                
            right -= 1
        print right, left
        return (right - left)
        """
