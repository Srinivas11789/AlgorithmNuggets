class Solution:
    def reverse(self, x: int) -> int:

        n = 2**31

        result = 0
        negate = False
        if x < 0:
            negate = True
            x = abs(x)

        y = x
        places = 1
        while y >= 10:
            places = places * 10
            y = y//10
        
        print(places)
        
        while x:
            temp = x%10
            x = x//10
            print(temp, x, places)
            if temp == 0:
                places = places//10
                if places == 0:
                    places = 1
                continue
            result += temp * places
            print(result)
            places = places//10

        if negate:
            result = -result
        
        if result < -n or result > n:
            return 0

        return result

