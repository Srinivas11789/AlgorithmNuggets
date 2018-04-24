class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        # --> 100 pass hashmap solution
        # Using hashmap
        counts = {}
        n = len(s)
        for i in range(n):
            if s[i] not in counts:
                counts[s[i]] = [i,0]
            counts[s[i]][1] += 1
        first = n+1
        for k,v in counts.items():
            if v[1] == 1 and v[0] < first:
                first = v[0]
        if first != n+1:
            return first
        else:
            return -1
        """
        """
        # Pythonic easy solution, Time Limit Exceeded
        n = len(s)
        for i in range(n):
            if s.count(s[i]) == 1:
                return i
        return -1
        """
        # 100 pass - when a easy pythonic way approach does not work for you, resort to trying to reduce the combinations rather than a completely new logic. Using set would have reduced the time for the program to pass all the cases. 
        # Modify pythonic to eradicate duplicates and reduce the check using set(), but set sorts the alphbets as well hence first occurrence fetch logic should be introduced
        count1 = []
        for char in set(s):
            if s.count(char) == 1:
                count1.append(s.index(char))
        if count1:
            return sorted(count1)[0]
        else:
            return -1
        """
        # non pythonic - but a little flawed logic
        n = len(s)
        select = 0
        count = 0
        i = 0
        while i < n:
                if s[i] == s[select]:
                    print s[i], s[select]
                    count += 1
                if count > 1:
                    visited.append(i)
                    select += 1
                    i = select
                    count = 0
                else:
                    i += 1
        if count == 1:
            return select
        else:
            return -1
        """

