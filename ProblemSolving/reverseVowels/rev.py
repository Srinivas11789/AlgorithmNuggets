class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        # Logic 1 = this logic replaces only the vowel to the last existing, but actual reverse is required
        s = list(s)
        v = ['a','e','i','o','u','A','E','I','O','U']
        prev = None
        n = len(s)
        for i in range(n):
            if s[i] in v:
                    if prev == None:
                        prev = i
                    else:
                        s[prev],s[i] = s[i],s[prev]
                        prev = i
        return "".join(s)
        """
        """
        # Logic2 - Two list solution - 100 Pass with list ds
        s = list(s)
        v = ['a','e','i','o','u','A','E','I','O','U']
        n = len(s)
        vowels = []
        indices = []
        for i in range(n):
            if s[i] in v:
                vowels.append(s[i])
                indices.append(i)
        for i,v in zip(indices, vowels[::-1]):
            s[i] = v
        return "".join(s)
        """
    
        # Logic 3 - two pointer solution - 100 Pass with only variable ds
        s = list(s)
        v = ['a','e','i','o','u','A','E','I','O','U']
        n = len(s)
        p1 = 0
        p2 = n-1
        while p1 < p2:
            if s[p1] in v and s[p2] in v:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            if s[p1] not in v:
                p1 += 1
            if s[p2] not in v:
                p2 -= 1
        return "".join(s)
                    
                    
            
