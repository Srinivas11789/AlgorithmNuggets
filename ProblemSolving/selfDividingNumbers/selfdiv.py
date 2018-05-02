class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        while left < right+1:
            l = list(str(left))
            count = 0
            for ch in l:
                if int(ch) != 0 and left%int(ch) == 0:
                    count += 1
            if count == len(l):
                result.append(left)
            left += 1
        return result
            
