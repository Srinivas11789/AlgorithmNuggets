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
        
        # Binary Search is better
        left = 0
        right = n
        while left < right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            
            if right-left == 1:
                if isBadVersion(left):
                    return left
                else:
                    return right
        
        return right
        
        # O(N) - You can go front or backwards both would be n --> we need to reduce it
        """
        i = 0
        while i < n:
            if isBadVersion(i):
                return i
            i += 1
        return i
        """
