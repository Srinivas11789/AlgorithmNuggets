class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        """
        # Bruteforce
        import itertools
        result = set()
        maxi = target//min(candidates)
        #print(maxi)
        for i in range(1, maxi+1):
            for comb in itertools.product(candidates, repeat=i):
                if sum(comb) == target:
                    comb = tuple(sorted(comb))
                    result.add(comb)
        return list(result)
        """
        
        def backtrack(result, temp, candidates, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                result.append(temp)
                return
            else:
                for i in range(start, len(candidates)):
                    backtrack(result, temp+[candidates[i]], candidates, remain-candidates[i], i)
        
        
        candidates = sorted(candidates)
        result = []
        backtrack(result, [], candidates, target, 0)
        return result
        
