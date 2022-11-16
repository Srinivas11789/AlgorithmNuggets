# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n
        if left == right:
            return left

        while left < right:
            mid = (left+right)//2
            gues = guess(mid)
            if gues == -1:
                right = mid-1
            elif gues == 1:
                left = mid+1
            else:
                return mid

            if guess(left) == 0:
                return left
            elif guess(right) == 0:
                return right

        return -1
