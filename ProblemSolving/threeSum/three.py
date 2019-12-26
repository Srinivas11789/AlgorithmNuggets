class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Logic 1: Bruteforce all three numbered groups to sum up to 0 - Time limit exceeded, all other tcs passed
        """
        import itertools
        result = set()
        for group in itertools.combinations(nums, r=3):
            uniq = tuple(sorted(group))
            if len(uniq) == 3 and uniq not in result and sum(uniq) == 0:
                result.add(uniq)
        return result
        """
        
        # Logic 2: Backtrack recursively -- Make optimal choice to backtrack -  Time limit exceeded, all other tcs passed
        """
        def backtrack(array, choices, chosen_ones):
            #print(array, choices, chosen_ones)
            if choices and len(choices) == 3:
                sumi = sum(choices)
                key = tuple(sorted(choices))
                if sumi == 0 and key not in choices:
                    chosen_ones.add(key)
                return
            for i in range(len(array)):
                if len(choices) < 3:
                    backtrack(array[:i]+array[i+1:], choices + [array[i]], chosen_ones)
            return chosen_ones
        return backtrack(nums, [], set())
        """
        
        # Logic 2(1/2) -> optimize the backtrack logic
        # a + b = -c ( conversion to a 2 sum problem is the best idea referring to https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation)
        """
        def backtrack(array, target, choices, chosen_ones):
            if choices and len(choices) == 2:
                sumi = sum(choices)
                key = tuple(sorted(choices+[target]))
                if sumi == -target and key not in chosen_ones:
                    chosen_ones.add(key)
                return
            for i in range(len(array)):
                if target == None:
                    backtrack(array[i+1:], array[i], choices, chosen_ones)
                else:
                    if len(choices) < 2:
                        backtrack(array[i+1:], target, choices + [array[i]], chosen_ones)
            return chosen_ones
        nums.sort()
        return backtrack(nums, None, [], set())
        """
        
        # Logic 3: Iterative method + convert to 2Sum 2pointer logic + Equality decision to obtain unique combinations
        
        # sort to make things easier to decide
        nums.sort()
        
        # Variable declaration
        N = len(nums)
        result = []
        
        # Convertion to 2 sum logic --> a + b + c = 0 --> a + b = -c 
        # * For each number we set it as -c and continue
        for i in range(N):
            
            # Eliminate equality or same combinations
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Set the target
            target = -nums[i]
            
            # Solve with 2 Sum logic with 2 pointer logic
            left = i+1
            right = N-1
            while left < right:
                current_sum = nums[left]+nums[right]
                if current_sum == target:
                    result.append([nums[left], nums[right], -target])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            
        return result
            
            
        
        
                
        
        
