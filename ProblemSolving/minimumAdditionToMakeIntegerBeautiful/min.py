class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        
        def calcSumOfDigits(k):
            sumOfDigits = 0
            while k:
                i = k%10
                k = k//10
                sumOfDigits += i
            return sumOfDigits
        
        s = calcSumOfDigits(n)
        if s <= target:
            return 0
        
        """
        # Logic1: n iteration
        for i in range(10**12+1):
            t = calcSumOfDigits(n+i)
            if t <= target:
                return i
        
        return 0
        """
        
        # Logic 2: Make zeros from unit place
        carry = 0
        chk = n
        remaining = []
        while chk:
            i = chk%10
            chk = chk//10
            remaining += [10-i]
        
        chk = n
        add = 0
        total = 0
        for i in range(len(remaining)):
            ind = i
            extra = 10**ind
            if extra == 0:
                extra = 1
            if extra > 1:
                remaining[i] = remaining[i]-1
            add = (remaining[i])*extra
            total += add
            chk += add
            print(total, chk,add, ind, extra,remaining)
            if calcSumOfDigits(chk) <= target:
                return total
            
        return 0
            
        
