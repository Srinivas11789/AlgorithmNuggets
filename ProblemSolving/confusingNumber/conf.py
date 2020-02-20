# Logic 1: Integer based with no type conversion - 96.56% faster
# * create a new number and check, also eliminate if denylist exists

class Solution:
    def confusingNumber(self, N: int) -> bool:
        old = N
        new = 0
        confusing = {
            0: 0,
            1: 1,
            9: 6,
            6: 9,
            8: 8
        }
        while N:
            current = N%10
            if current in set([2,3,4,5,7]):
                return False
            else:
                new = new*10 + confusing[current]
            N = N//10
        print(old, new)
        if old != new:
            return True
        else:
            return False


# Try without creating the new number --> Fail pending...
"""
class Solution:
    def confusingNumber(self, N: int) -> bool:
        same_chances = set([0,1,8])
        count = 0
        digits = 0
        while N:
            current = N%10
            if current in set([2,3,4,5,7]):
                return False
            elif current in same_chances:
                count += 1
            digits += 1
            N = N//10
        if count == digits:
            return False
        return True
"""

    
