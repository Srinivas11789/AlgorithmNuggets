class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        # 1. Naive array iteration for each i item (o(N)**2) --> time limit exceeded 26/59
        """
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                result[j] += abs(nums[i] - nums[j])
        return result
        """

        # 2. Technique --> operate over left and right sum - 100 pass
        # logically, leverage sorted order to understand that (a-b) + (a-c) + (a-d) = sum(a,b,c) will allow to group a's to 3a - b - c - d when a > b > c > d
        presum = 0
        pastsum = sum(nums)
        result = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            test1 = abs(presum - (i * nums[i]))
            test2 = abs(pastsum - ((len(nums)-i) * nums[i]))
            if i == 0 or i == len(nums)-1:
                result[i] = max(test1, test2)
            else:
                result[i] = test1 + test2
            presum += nums[i]
            pastsum -= nums[i]
        return result

