class Solution:
    def check(self, nums: List[int]) -> bool:

        def findDivergedAtPos(nums: List[int]) -> (bool, int):
            diverge = -2
            for i in range(1, len(nums)):
                if nums[i] >= nums[i-1]:
                    continue
                if diverge != -2:
                    return True, diverge 
                diverge = i
            if diverge > -2:
                return True, diverge
            return False, 0

        diverged, pos = findDivergedAtPos(nums)
        if diverged and pos == -2:
            return False

        sort_nums = nums[pos:] + nums[:pos]
        diverged, pos = findDivergedAtPos(sort_nums)
        print(diverged, pos, sort_nums)
        if pos == 0 and not diverged:
            return True

        return False
