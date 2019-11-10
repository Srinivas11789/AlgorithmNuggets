class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Rotate to themself
        # 0,1,8
        # Rotate to Each other
        # 2,5 
        # 6,9
        # Others do not rotate to valid numbers at all
        
        result = []
        for n in range(N+1):
            new = ""
            for char in str(n):
                if char in ["0","1","8"]:
                    new += char
                elif char == "6":
                    new += "9"
                elif char == "9":
                    new += "6"
                elif char == "2":
                    new += "5"
                elif char == "5":
                    new += "2"
                else:
                    break
            if str(n) != new and len(str(n)) ==len(new):
                result.append(n)
        return len(result)
        
"""
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        rot = {
            0: 0,
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            8: 8,
            9: 6
        }
        
        def good_number(num):
            result = ""
            for i in str(num):
                if int(i) not in rot:
                    return False
                else:
                    result += str(rot[int(i)])
            #print(num , result)
            if int(result) != num:
                return True
            else:
                return False

        ans = []
        for i in range(1, N+1):
            if good_number(i):
                ans.append(i)
        print(ans)
        return len(ans)
"""        
