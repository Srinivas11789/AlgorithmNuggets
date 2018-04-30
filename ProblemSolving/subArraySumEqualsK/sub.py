class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        # Not quite working - something wrong
        # Brute force solution
        n = len(nums)
        result = []
        for j in range(0,n):
            for i in range(n):
                    if nums[i] == k:
                        print nums[i]
                        result.append(nums[i])
                    if i+j <= n and sum(nums[i:i+j]) == k:
                        print nums[i:i+j]
                        result.append(nums[i:i+j])
        return len(result)
        """
        """
        # Running Sum Technique - 100pass
        
        # Variable to calculate the sum as we progress through the array
        sumi = 0
        # Hashmap to maintain the sum data and respective counts
        hashmap = {}
        # Variable to hold the result
        result = 0
        
        for i in nums:
            # Running sum calculation as we progress through the array
            sumi += i
            
            #
            result += hashmap.get(sumi-k,0) + (1 if sumi == k else 0)
            
            # Update the sum entry present in the hashmap
            hashmap[sumi] = hashmap.get(sumi,0) + 1
            
        return result
        """
    
        # 100 pass - Running Sum technique and minus k to find its exitence and increase count
        # As we progress through the array finding the sums => sum(a[5]) - k = sum(a[2]) which provides sum(3,4) 
        
        
        sumi = 0
        # A dictionary to count the entries as values and respective entries as key
        hashmap = collections.Counter()
        result = 0
        # For 0 length 
        hashmap[0] += 1
        n = len(nums)
        for i in range(n):
            sumi += nums[i]
            if sumi-k in hashmap:
                result += hashmap[sumi-k]
            hashmap[sumi] += 1
        return result
            
