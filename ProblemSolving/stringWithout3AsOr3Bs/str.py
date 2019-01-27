class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        
        # Output S
        # * len(S) = A+B
        # * len(As) = len(a) and len(Bs) = len(b)
        # * "No aaa and no bbb occurences"
        result = ""
        
        # Logic: Known String Logic (Leverage known string as you are constructing the string) - 100 pass lt easy
        # when A or B is way greater, we need the other to break the sequence so the conditions are satisfied
        # * We do not have the privilege to use either of them as we traverse
        #   - Instead use the sequence you know for sure wont have a conflict, that is `aab` or `bba`
        #   - Reference: https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/227167/Python3-short-and-simple
        
        # Other than one being zero, both should have a minimum of `2` so that know string assumption works
        while A > 0 and B > 0:
            if A > B:
                result += "aab"
                A -= 2
                B -= 1
            elif B > A:
                result += "bba"
                B -= 2
                A -= 1
            else:
                result += "ba"
                A -= 1
                B -= 1
        
        # Any on A or B being 0 condition
        result += "a"*A
        result += "b"*B
        
        return result
        
        # Previous Tries - Faied logic below
        # Try one different method, rearrange after string creation
        """
        # Create string with necessary string length and count of a and b
        if A > B:
            result = ["a"]*A
            remaining = ["b"]*B
        else:
            result = ["b"]*B
            remaining = ["a"]*A
        
        # Rearrange
        i = 2
        if len(result) > 2:
            while i < len(result):
                if result[i] == result[i-1] == result[i-2]:
                        result = result[:i]+[remaining.pop()]+result[i:]
                i += 1
        
        print result
        if remaining:
                result.extend(remaining)
        
        return "".join(result)
        """
           
        # Add 2 times or 1 time based on the choices
        """
        result = ""
        
        while A > 0 or B > 0:
            if A > B:
                if A > 2 and "".join(result[-1:]) != "a":
                    result += "aa"
                    A -= 2
                elif A > 0 and "".join(result[-2:]) != "aa":
                    result += "a"
                    A -= 1
            else:
                if B > 2 and "".join(result[-1:]) != "b":
                    result += "bb"
                    B -= 2
                elif B > 0 and "".join(result[-2:]) != "bb":
                    result += "b"
                    B -= 1
                
        return result
        """
                
        # Add one/more time based on the choice
        """
        result = ""
        while A > 0 or B > 0:
            while A > 0 and ((len(result) < 2) or (len(result) >= 2 and list(set(result[-2:]))[0] != "a")):
                    print result, list(set(result[-2:]))[0]
                    result += "a"
                    A -= 1
            while B > 0 and ((len(result) < 2) or (len(result) >= 2 and list(set(result[-2:]))[0] != "b")):
                    result += "b"
                    B -= 1
        return result
        """   
