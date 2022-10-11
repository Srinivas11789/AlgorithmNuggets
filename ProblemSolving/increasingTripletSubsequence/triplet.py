class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        curr_maxis = [-float('inf'), -float('inf'), -float('inf')]
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(3):
                if nums[i] >= curr_maxis[j]: 
                    curr_maxis[j] = nums[i]
                    curr = j
                    break
            print(curr_maxis)
            if curr == 2 and curr_maxis != -float('inf'):
                return True

        print(curr_maxis)
        return False
