class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Initial variables to use
        n = len(nums)
        counts = {}
        maxi = 0
        interval = set()
        select = []
        
        # Made up my required dictionary of all the details -> count, [indices], intervals_of_indices with O(n) traversal, also found the maximum
        for i in range(n):
            if nums[i] not in counts:
                counts[nums[i]] = [0,[],0]
            counts[nums[i]][0] += 1
            counts[nums[i]][1].append(i)
            counts[nums[i]][2] = counts[nums[i]][1][-1]-counts[nums[i]][1][0]
            if counts[nums[i]][0] >= maxi:
                maxi = counts[nums[i]][0]
            
        # Operate on the maximum values
        for k,v in counts.items():
            if v[0] == maxi:
                select.append(k)
                interval.add(v[2])
        
        # Return the intervals calculated
        print interval, select
        if not list(interval):
            return 1
        return sorted(interval)[0]+1
    
        """
            if counts[nums[i]][0] >= maxi:
                maxi = counts[nums[i]][0]
                if nums[i] not in select:
                    select.append(nums[i])
                if counts[nums[i]][2] > 0:
                    interval.add(counts[nums[i]][2])

        print interval
        if not list(interval):
            return 1
        return list(interval)[0]+1
        """
        
        """
                   if counts[nums[i]][0] >= maxi:
                maxi = counts[nums[i]][0]
                if counts[nums[i]][2] > 1 and counts[nums[i]][2] < interval:
                    interval = counts[nums[i]][2]
                if nums[i] not in select:
                    select.append(nums[i])
                    
                    
                    if len(select) > 1:
            for v in select:
                if not interval:
                    interval = counts[v][2]
                elif counts[v][2] < interval:
                    interval = counts[v][2]
        #print maxi, interval, counts[select[1]][1]
        """
        
        
        """
        # TimeLimitExceeded
        # Initial variables to use
        n = len(nums)
        counts = {}
        maxi = 0
        select = []
        
        # Made up my required dictionary of all the details -> count, [indices] with O(n) traversal, also found the maximum
        for i in range(n):
            if nums[i] not in counts:
                counts[nums[i]] = [0,[]]
            counts[nums[i]][0] += 1
            counts[nums[i]][1].append(i)
            if counts[nums[i]][0] >= maxi:
                maxi = counts[nums[i]][0]
                if nums[i] not in select:
                    select.append(nums[i])
        
        #print counts, maxi, select
        # Degree of the total array is maxi
        
        # Scenario for multiple degree elements
        # Select the least length element as the maximum if there are multiple maximum elements with same number of occurences
        least_length_substring = 600000
        i = 0
        final = None
        while len(select) > 0:
                if (counts[select[i]][1][-1] - counts[select[i]][1][0]) < least_length_substring:
                    least_length_substring = counts[select[i]][1][-1] - counts[select[i]][1][0]
                    final = select.pop(i)
        
        #print final,least_length_substring
        
        return least_length_substring+1
        """
        
        
        """
        def degree(nums):
            maxi = 0
            select = None
            for char in set(nums):
                val = nums.count(char)
                if val > maxi:
                    maxi = val
                    select = char
            return [maxi,char]
        
        for num in nums:
        """
            
            
        
