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
                
                
            
            
        
