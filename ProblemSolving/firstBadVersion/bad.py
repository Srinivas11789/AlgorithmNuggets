# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # BruteForce error ==> Memory Error
        select = n//2
        
        if isBadVersion(select):
            for i in range(select):
                if isBadVersion(i) == 0:
                    return i
        else:
            for i in range(select,n):
                if isBadVersion(i) == 0:
                    return i
        """
        
        # Evident from some discussion and solution - Use Binary search of going with the mid points
        # Similar to the custom solution generated before in the guessNumber problem
        
        # Implement a binary search of going throught the mid points
        
        # Setting the high and low for the ranges. <Take care of not using 0 here corresponding to the array index>
        high = n
        low = 1
        
        # Iterating until the mid, if a match is found
        while low < high:

            # Mid point logic
            select = low + (high-low)//2
            
            # If bad version has already been hit, set high as the current index, as the first would surely exist before that
            if isBadVersion(select):
                    high = select
            else:
                # If bad version is not yet visited, increase the low to current + 1 as the first occurence will happen at any index from this index
                low = select + 1
        
        # Return the low which is the selected
        return low
            
            
        
