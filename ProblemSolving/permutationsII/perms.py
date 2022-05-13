class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # Logic 1: using itertools
        """
        perms = []
        visited = set()
        for i in itertools.permutations(nums, r=len(nums)):
            if i not in visited:
                perms.append(i)
                visited.add(i)
        return perms
        """
        
        # Logic 2: backtrack
        self.perms = []
        self.visited = set()
        
        def backtrack(nxts, current, curr_int):
            if not nxts:
                if curr_int not in self.visited:
                    self.perms.append(current)
                    self.visited.add(curr_int)
            
            for i in range(len(nxts)):
                others = nxts[:i]
                if i+1 < len(nxts):
                    others += nxts[i+1:]
                backtrack(others, current + [nxts[i]], nxts[i] + 10*curr_int)
            
        backtrack(nums, [], 0)
        return self.perms
