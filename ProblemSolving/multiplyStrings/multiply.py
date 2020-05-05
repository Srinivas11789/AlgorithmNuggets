# Logic 1: Naive method of using dictionary to map string and numbers representation of integers ( 0-9) - 80% faster
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def numberFromString(n, numStr):
            num = 0
            l = len(n)-1
            for i in range(l+1):
                num += 10**(l-i) * numStr[n[i]]
            return num
        
        # 1. String number dictionary - it can be hardcoded without using str() one time
        numStr = {}
        for i in range(10):
            numStr[str(i)] = i
        strNum = {}
        for i in range(10):
            strNum[i] = str(i)
        
        # 2. Construct number from string
        prod = numberFromString(num1, numStr)*numberFromString(num2, numStr)
        
        # 3. Construct string after product
        result = ""
        while prod:
            result = strNum[prod%10] + result
            prod = prod//10
        if result == "" and prod == 0:
            return "0"
        return result
