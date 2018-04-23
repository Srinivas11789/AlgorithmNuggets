class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initial logic - get count of respective character for each of the strings, sort the counts into a list and compare both such list to verify if they are equal
        # Every index also is taken into account with the count
        
        # Second logic - second logic
        sc = {}
        tc = {}
        n = len(s)
        # Same length strings
        for i in range(n):
            if s[i] not in sc:
                sc[s[i]] = []
            sc[s[i]].append(i)
            if t[i] not in tc:
                tc[t[i]] = []
            tc[t[i]].append(i)
        
        
        if sorted(tc.values()) == sorted(sc.values()):
            return True
        else:
            return False
