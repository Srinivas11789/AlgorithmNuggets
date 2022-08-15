class Solution:
    def intToRoman(self, num: int) -> str:
        
        romanNum = ""
        
        roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        number = []
        
        while num:
            n = num%10
            number = [n]+number
            num = num//10
        
        while number:
            n = number.pop(0)
            r = 10**len(number)
            ns = n*r
            
            if ns in roman:
                romanNum += roman[ns]
                print(romanNum, n, r, ns)
                continue
            
            print(romanNum, n, r, ns)
            
            if n == 4:
                romanNum += roman[r] + roman[5*r]
            elif n == 9:
                romanNum += roman[r] + roman[10*r]
            elif n > 5:
                romanNum += roman[5*r] + roman[r*1]*(n-5)
            else:
                romanNum += roman[1*r]*(n)

        return romanNum
