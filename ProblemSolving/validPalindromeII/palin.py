class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        # --> Thoughts
        # Logic 1: Iterate the string remove each character and checking whether they are palindome
        # Logic 2: Find the char which does not exist in the other string and then check if palindrome or not, reduces the number of comparisons
        
        # Default palindrome check. at-most 1 ==> initially 0 removal condition
        if s == s[::-1]:
            return True
        
        
        # Time limit exceeded for this logic
        # at-most 1 condition
        for i in range(len(s)):
            new = s[:i]+s[i+1:]
            if new == new[::-1]:
                return True
        return False
        """
        
        # Logic 2 reiterate: Count the character that occur only once and remove them to check
        # at-most 1 condition
        
        """
        # Wrong logic
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
            
        for key,val in counts.items():
            if val%2 != 0:
                index = s.index(key)
                new = s[:index]+s[index+1:]
                if new == new[::-1]:
                    return True
        return False
        """        
        
        # Logic 3 --> Use left and the right pointers to traverse through the string and find palindrome
        # Reference form yangshun from discussion
        
        # Two pointers - one at the front and one at the end
        left, right = 0, len(s)-1
        
        # Looping while left is lesser than right
        while left < right:
            
            # As it is a palindrome, the characters at both the ends should be equal as we traverse, if they are not equal then required check should be performed for palindrome when the character is removed.
            if s[left] != s[right]:
                # When they are not equal, create 2 substring with left element and without left element
                left_sample, right_sample = s[left:right], s[left+1:right+1]
                
                # Check the substrings to be palindrome including both the substrings, if anyone is palindrome or both are then True else False
                return left_sample == left_sample[::-1] or right_sample == right_sample[::-1]
            
            # Looping condition
            left, right = left+1, right-1
        
        # Default condition to return True for all cases
        return True
                
                
        
       
            
        
        
            
