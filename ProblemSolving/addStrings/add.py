class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        """
        # As the explanation says - donot use int typecast - solution not correct
        # Pythonic solution - 100 pass
        return str(int(num1)+int(num2))
        """
        
        # Could perform each digit addition and keep track of the carry
        # how to convert each digit string to integer and back??? Using ord to conver to hex representation throws - 48, 49, 50 for the 0,1,2 range of numbers as strings. Converting them such that "1" => ord("1")-ord("0") ==> 49-48 => 1, converts the string into integer representation of the same number 
        
        # Reversing the number to add from units place
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = len(num1)
        m = len(num2)
        
        # Appending zeros to equalize the lengths
        if n > m:
            payload = "0"*(n-m)
            num2 = num2+payload
            maxi = n
        else:
            payload = "0"*(m-n)
            num1 = num1+payload
            maxi = m
        
        # sumi - calculate the total sumi
        # current - current sum calculation
        # carry - to hold the carry forward
        result = []
        carry = 0
        for i in range(maxi):
                #print num1[i],num2[i]
                sumi = (ord(num1[i])-ord("0")) + (ord(num2[i])-ord("0")) + carry
                current = sumi%10
                carry = sumi//10
                #print sumi, current, carry
                result.append(str(current))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])
        
                
    
