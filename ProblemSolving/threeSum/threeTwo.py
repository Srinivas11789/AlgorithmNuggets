class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Logic 1: Convert to multiple 2sum subprobs and solve
        def twoSum(nums, target):
            cache = {}
            result = []
            visited = set()
            for i in range(len(nums)):
                final = target - nums[i]
                if final not in cache:
                    cache[final] = []
                cache[final].append(i)

            for i in range(len(nums)):
                if nums[i] not in cache:
                    continue
                for j in cache[nums[i]]:
                    if i == j:
                        continue
                    chktmp = (nums[i], nums[j])
                    if chktmp in visited:
                        continue
                    visited.add(chktmp)
                    result.append([i, j])
            print(target, result)
            return result
            
        result = []
        indexTargets = {}
        for i in range(len(nums)):
            target = 0 - nums[i] 
            if target not in indexTargets:
              indexTargets[target] = []
            indexTargets[target].append(i)


        visited = set()
        for target in indexTargets:
            targetCombs = twoSum(nums, target)
            #print(indexTargets[target], targetCombs)

            for o in indexTargets[target]:
                for t in targetCombs:
                    tmp = [nums[o]]
                    tmpS = set([nums[o]])
                    tS = set(t)
                    if o in tS:
                        continue
                    for i in t:
                        tmp.append(nums[i])
                    tmpS.update(tS)
                    chktmp = tuple(sorted(tmp))
                    if chktmp not in visited and sum(tmp) == 0:
                      visited.add(chktmp)
                      result.append(chktmp)

        return result
                


