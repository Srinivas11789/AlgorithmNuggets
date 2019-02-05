class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        # Logic: This iterates through all combination, works 100% but 35ms fast only.
        
        # Itertools for using product, combinations or permutations
        import itertools
        
        # Result array to hold all the valid combinations
        result = []
        
        # As repeated elements can be unlimited, we start the iteration with minimum element in the array that adds up to the target
        mini = min(candidates)
        n = target//mini
        
        # Using combinations with replacement --> to have all the combination of length r with repeated elements, and check if sum adds up to the target
        for i in range(n, 0, -1):
            for comb in itertools.combinations_with_replacement(candidates, r=i):
                if sum(comb) == target:
                    result.append(comb)
        return result
        
    
        """
        # Another Logic with Recursive strategy
        # Reference: https://leetcode.com/problems/combination-sum/discuss/232167/python-simple-backtracking
        
        result = []
 
        def recursive_combinations(temp, index):
        
            if sum(temp) > target:
                return
            elif sum(temp) == target:
                temp = sorted(temp)
                if temp not in result:
                    result.append(temp)
                return
            
            for i in range(index, len(candidates)):
                recursive_combinations(temp+[candidates[i]], index)
        
        recursive_combinations([], 0)
        return result
        """ 
        
"""
### Pending...

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ### Works for smaller target values
        # Sorted Logic
        candidates = sorted(candidates)
        
        result = []
        
        # Iterate through each candidate
        n = len(candidates)
        ans = []
        
        for i in range(n):
            
            # Repeated Condition
            while sum(ans) < target:
                ans.append(candidates[i])
            if sum(ans) == target:
                if ans not in result:
                    result.append(ans)
            ans = []
            
            # Combination of other numbers
            if i+1 < n-1:
                for j in range(i+1,n):
                    print candidates[i],candidates[j]
                    cur = candidates[i]+candidates[j]
                    if target-cur in candidates:
                        array = sorted([candidates[i], candidates[j], target-cur])
                        if array not in result:
                            result.append(array)
                    if target-cur == 0:
                        array = sorted([candidates[i], candidates[j]])
                        if array not in result:
                            result.append(array)
            else:
                j = n-1
                print candidates[i],candidates[j]
                cur = candidates[i]+candidates[j]
                if target-cur in candidates:
                        array = sorted([candidates[i], candidates[j], target-cur])
                        if array not in result:
                            result.append(array)
                if target-cur == 0:
                        array = sorted([candidates[i], candidates[j]])
                        if array not in result:
                            result.append(array)
            
            
        return result
                
"""                
            
            
        
