class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # Contiguous SubArray
        
        # 100 pass - Reiterating the same logic as below with lower sum or div or max calculation 
        
        if k > len(nums):
            return sum(nums)/float(k)
        
        i = k
        maxi = sum(nums[:k])
        sumi = maxi
        n = len(nums)
        while i < n:
            
            # Logic of iterating from k adding each element and removing the last element of contiguous array
            sumi = sumi + nums[i] - nums[i-k]
            if sumi > maxi:
                    maxi = sumi
            i += 1
            
            """
            # Logic of constructing an array everytime of k size and performing the operation, perfectky correct but no time optimized
            if i+k > n:
                break
            select = nums[i:i+k]
            sumi = sumi - nums[i-1] + select[-1]
            if sumi > maxi:
                    maxi = sumi
            i += 1
            if i+k > n:
                break
            """

        return maxi/float(k)
        
        
        """
        # Logic 1: Correct Logic and Solution - Time Limit Exceeded
        # Iterating only until the contiguous array is lesser than the total length of the array
        
        i = 0
        maxi = -60000000
        sumi = None
        
        if k > len(nums):
            return sum(nums)/float(k)
        
        while i < len(nums):
            print i
            if i+k > len(nums):
                break
            #if i+k <= len(nums):
            select = nums[i:i+k]
            #print select
            if not sumi:
                sumi = sum(select)
            else:
                sumi -= nums[i-1]
                sumi += select[-1]
            if sumi/float(k) > maxi:
                    maxi = sumi/float(k)
            i += 1
            if i+k > len(nums):
                break
            #else:
            #    i += 1
        return maxi
        """
             
        """
        # Non contiguous subarray solution - try contiguous ssubarray technique
        import itertools
        maxi = -60000000
        for comb in itertools.combinations(nums, r=4):
            #print comb
            value = sum(comb)//len(comb)
            if value > maxi:
                print maxi, comb
                maxi = value
        return maxi
        """
