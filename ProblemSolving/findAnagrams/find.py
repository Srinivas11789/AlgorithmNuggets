class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # Sliding window technique - A str of length p slides over the string s matching possible anagrams
        # reference from user RogerFederer
        
        # Length Calculation
        np = len(p)
        ns = len(s)
        
        # Corner cases handle
        if np > ns or not p or not s:
            return []
        
        # Dictionary Creation to reduce access times
        import collections
        cp = collections.Counter(p)
        cs = collections.Counter(s[:np]) # only the first three characters
        r = ns - np + 1 # iteration happens from 0 hence +1
        result = []
        
        for i in range(r):
            #print cs, s[i]
            # Sliding window, next char added to the dictionary
            if i > 0:
                cs[s[i+len(p)-1]] += 1
            
            # Anagram check
            if cp == cs:
                result.append(i)
                
            # Remove the current char to progress the window further 
            cs[s[i]] -= 1
            
            # Character becomes zero then delete
            if cs[s[i]] == 0:
                del cs[s[i]]
                
        return result
               
        """
        # With repeated "a" for 1000 times as input, time limite exceeded
        result = []
        s = list(s)
        ns = len(s)
        p = sorted(p)
        n = len(p)
        i = 0
        if n > ns:
            return []
        while i < ns:
            # Failing because it checks for non existing characters as we move along n times
            if s[i] in p and i+n <= ns:
                #print i, i+n
                if p == sorted(s[i:i+n]):
                    print i, i+n
                    result.append(i)
                i += 1
            else:
                i += 1
        return result
        """
        
        # Python hacky solution
        # Count the number of times abc occurs in the list
        
        
        ## New day New logic - 
        
        # 
        
        """
        # Anagram function checker _ logic not 100 percent correct
        def anagram(string, check):
            for i in range(len(string)):
                curr = string[i:]+string[:i]
                print check, curr
                if curr == check:
                    return True
            if string[::-1] == check:
                return True
            return False
        
        #print anagram("cba","abc")
        
        if len(p) > len(s):
            return []
        
        result = []
        for i in range(len(s)):
            if s[i] in p:
                if i+len(p) <= len(s):
                    if s[i:i+len(p)] in check:#if anagram(s[i:i+len(p)], p):
                        result.append(i)
        return result
        """
        
        """
        # Build all the combinations list - Brute force and correct but Time Limit Exceeded
        
        if len(p) > len(s):
            return []
        
        # Anagrams build
        import itertools
        check = []
        for c in itertools.permutations(list(p), r=len(p)):
            check.append("".join(c))
        print check
        
        result = []
        for i in range(len(s)):
            if s[i] in p:
                if i+len(p) <= len(s):
                    if s[i:i+len(p)] in check:#if anagram(s[i:i+len(p)], p):
                        result.append(i)
        return result
        """
        
        
        
                
