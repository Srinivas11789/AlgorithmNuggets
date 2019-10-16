class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits)-1
        carry = 1
        while i >= 0 and carry:
            add = digits[i] + carry
            digits[i] = add%10
            carry = add//10
            i -= 1
        if carry:
            digits = [carry] + digits
        return digits
        
