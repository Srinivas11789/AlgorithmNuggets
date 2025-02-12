class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sumOfDigits(num):
            s = 0
            while num:
                s += num%10
                num = num//10
            return s

        numsSumDigits = {}
        cacheSod = {}
        result = -1
        computed = set()

        nums.sort(reverse=True)

        for i in range(len(nums)):
            if nums[i] in cacheSod:
                sd = cacheSod[nums[i]]
            else:
                sd = sumOfDigits(nums[i])
                cacheSod[nums[i]] = sd
            if sd in computed:
                continue
            if sd not in numsSumDigits:
                numsSumDigits[sd] = []
            #for s in numsSumDigits[sd]:
            #    result = max(result, s+nums[i])
            if len(numsSumDigits[sd]) == 1:
                result = max(result, numsSumDigits[sd][0] + nums[i])
                computed.add(sd)
            numsSumDigits[sd].append(nums[i])
        
        return result

