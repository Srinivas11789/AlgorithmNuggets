class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Logic 3: Retain the order and iterate across the same characters, remember we need to --> add in front, remove in back or replace the character one time
        # * they will surely match as we iterate else fail out - 100 pass 66% faster
        pointer1 = 0
        pointer2 = 0
        diff = 0
        if not s and not t:
            return False
        while pointer1 < len(s) or pointer2 < len(t):
            # 3. Out of index condition - exceeded one of the string
            if (pointer1 < len(s) and pointer2 >= len(t)):
                diff += 1
                pointer1 += 1            
                continue
            elif (pointer1 >= len(s) and pointer2 < len(t)):
                diff += 1
                pointer2 += 1
                continue

            # 1. Both characters are equal
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
                pointer2 += 1
                continue
            
            # When they are not equal
            diff += 1 # if not equal they are different
            
            # 2. Proceedingly they should be equal else fail
            if pointer1+1 < len(s) and s[pointer1+1] == t[pointer2]:
                pointer1 += 1
                continue
            elif pointer2+1 < len(t) and t[pointer2+1] == s[pointer1]:
                pointer2 += 1
                continue
            else: # They are not equal more than once, FAIL
                pointer1 += 1
                pointer2 += 1
                if diff > 1:
                    return False
                continue

        if diff == 1:
            return True
        else:
            return False

        # Logic 1: Does not work when the sorted order are different "ab vs bc" --> FAIL
        """
        s = sorted(s)
        t = sorted(t)
        n = len(s)
        m = len(t)
        if n > m:
            t += "0"*(n-m)
        else:
            s += "0"*(m-n)
        count = 0
        for i, j in zip(s, t):
            if i == 0 or j == 0:
                count += 1
            elif i != j:
                count += 1
            if count > 1:
                return False
        if count == 1:
            return True
        else:
            return False
        """
        
        # Logic 2: Find the Intersection
        # * finds the different string correctly but replace, add, delete rule fails! --> FAIL
        """
        import collections
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        if len(s) > len(t):
            for i in range(len(s)):
                if s[i] in tc:
                    sc[s[i]] -= 1
                    tc[s[i]] -= 1
                if sc[s[i]] == 0:
                    del sc[s[i]]
                if tc[s[i]] == 0:
                    del tc[s[i]]
            print(sc)
            if len(sc.keys()) == 1:
                return True
            else:
                return False
        else:
            for i in range(len(t)):
                if t[i] in sc:
                    tc[t[i]] -= 1
                    sc[t[i]] -= 1
                    if tc[t[i]] == 0:
                        del tc[t[i]]
                    if sc[t[i]] == 0:
                        del sc[t[i]]
            print(tc)
            if len(tc.keys()) == 1:
                return True
            else:
                return False
        """

