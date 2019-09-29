# Pending
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # Logic 1: Hacky way of using itertools - Time Limit Exceeded Obviously
        """
        import itertools
        for substring in itertools.permutations(s1, r=len(s1)):
            if "".join(substring) in s2:
                return True
        return False
        """
        
        # Logic 2: O(N) Iteration with dictionary copies of substring - Time Limit Exceeded
        """
        i = 0
        import collections
        c = collections.Counter(list(s1))
        temp = c.copy()
        start = None
        while i < len(s2):
            if s2[i] in temp and temp[s2[i]] > 0:
                temp[s2[i]] -= 1
                if start == None:
                    start = i
            else:
                temp = c.copy()
                if start != None:
                    i = start
                start = None
            if len(set(temp.values())) == 1 and list(set(temp.values()))[0] == 0:
                return True
            i += 1
        return False
        """
        
        # Logic 3: O(N) iterate, select index plus length and check equality - Time Limit Exceeded
        """
        s1 = sorted(s1)
        for i in range(len(s2)):
            #print(s1, sorted(s2[i:i+len(s1)]))
            if i+len(s1)-1 < len(s2) and sorted(s2[i:i+len(s1)]) == s1:
                return True
        return False
        """
        
        
        import collections
        c1 = collections.Counter(s1)
        i = 0
        while i < len(s2):
            #print(s1, sorted(s2[i:i+len(s1)]))
            if s2[i] in c1:
                if i+len(s1)-1 < len(s2) and collections.Counter(s2[i:i+len(s1)]) == c1:
                    return True
                else:
                    i += len(s1)
            else:
                i += 1
        s2 = s2[::-1]
        while i < len(s2):
            #print(s1, sorted(s2[i:i+len(s1)]))
            if s2[i] in c1:
                if i+len(s1)-1 < len(s2) and collections.Counter(s2[i:i+len(s1)]) == c1:
                    return True
                else:
                    i += len(s1)
            else:
                i += 1
        return False
        
        """
        # Logic 3: 2 Pointer Method
        left = None
        right = None
        for i in range(len(s2)):
        """
