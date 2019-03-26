class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        # Logic 2:
        # * Assumption is the array order should be maintained!!!!
        # * Almost all the logic in discussion follow total_sum + average method...
        # * This sounds interesting: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/262153/C%2B%2B-beat-98-68ms
        
        
        # Total sum
        total_sum = sum(A)
        
        # If the total cannot be divided into 3 exit
        if total_sum%3 != 0:
            return False
        
        # Average per section
        average = total_sum//3
        
        # Easy thing is there should be no change in order of the array - which I could not anticipate from the problem
        
        # Iterate to find the sum to average
        temp_sum = 0
        count = 0
        for i in A:
            temp_sum += i
            if temp_sum == average:
                count += 1
                temp_sum = 0
            if count > 3:
                return False
        
        # Only true if divided into 3 parts
        return count == 3
        
        # Logic1: Finding cube root to calculate - Wrong
        """
        # Total sum
        total_sum = sum(A)

        # Is total a perfect cube root?
        # power to 1/3
        temp = abs(total_sum)
        temp = temp**(1./3.)
        
        print total_sum, temp
        
        if temp:
            return True
        else:
            return False
        """
