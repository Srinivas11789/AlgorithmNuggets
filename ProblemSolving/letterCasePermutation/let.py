class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        
        # 100 pass - Nice logic
        # Create a combination iteration using itertools in python
        import itertools
        
        # Building a list with all possible combination that could occur
        comb = []
        for char in S.lower():
            if char.isalpha():
                comb.append([char.lower(), char.upper()])
            else:
                comb.append([char])
        
        result = []
        for comb in itertools.product(*comb):
            result.append("".join(comb))
        
        return result
        
    
        """
        # 100 pass too - Without itertools using recursion - from the discussion nice logic of recursion - by praviteja5
        
        # Same as above logic to add the combinations of [lower, upper] for character and [num] for integer, using recursion as we move through the iterating for the combinations and adding each combination into the iteration
        
        # Recursion Function - 
        def combinations(S, result, start, output):
            
            if start == len(S):
                result.append(output)
                return 
            
            if S[start].isalpha():
                control = [S[start].lower(), S[start].upper()]
            else:
                control = [S[start]]
            
            for j in range(len(control)):
                combinations(S, result, start+1, output + control[j])            
        
        # Driver
        result = []
        combinations(S, result, 0, "")
        return result
        """
        
        """
        # With increasing alphabet existence combinations increase
        # Number of letters found *2 would be the total combination <lowercase + uppercase>
        
        # Brute force - O(N) - Fails when alternating upper + lower combination occurs - tweak to make it consistent before processing, make everything lower and reason from there
        # Run once with lower and once with upper
        
    
        # Append all lowercase and all uppercase initially - Make the given string lowercase and Make the given string all upper
        S = S.lower()
        S1 = S.upper()
        
        result = [S] 
        
        # Check for all integers existence - when "12345" occurs there is only one combination
        if S1 not in result:
            result.append(S.upper())
        
        n = len(S)
        
        for i in range(n):
            # To check for a character could use ord() to find the ascii value lying between 67 or 97 for lower and upper cases
            # or could use isalpha() function
            
            if S[i].isalpha():
                
                # All upper case string into consideration, make each char to lowercase
                string1 = S1[:i]+S[i].lower()+S1[i+1:]
                if string1 not in result:
                    result.append(string1)
                    
                # All lower case string into consideration, make each char to uppercase
                string2 = S[:i]+S[i].upper()+S[i+1:]
                if string2 not in result:
                    result.append(string2)
        return result
        """
                
