class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        numset = set()

        for i in range(len(nums)):
            n = len(nums[i])
            numset.add(nums[i])

        comp = ["1"*n, "0"*n]
        for i in range(len(nums)):
            target = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(nums[i], comp[0]))
            if target not in numset:
                return target
            target = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(nums[i], comp[0]))
            if target not in numset:
                return target

        stack = ["0", "1"]
        while stack:
            curr = stack.pop(0)
            if len(curr) == n and curr not in numset:
                return curr
            if len(curr) > n:
                continue
            for i in ["0", "1"]:
                stack.append(curr+i)

        return ""

        
