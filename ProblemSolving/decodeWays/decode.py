class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Without literally solving - try using math and some memo - 78% faster
        # Ref: https://leetcode.com/problems/decode-ways/discuss/372420/Python-O(n)-time-O(1)-space-Detail-explanation-Turtle-Code
        if not s or s[0] == "0":
            return 0
        l1, l2, curr = 1, 1, 0
        for i in range(1, len(s)):
            if s[i] != "0":
                curr = l1
            if "10" <= s[i-1:i+1] < "27":
                curr += l2
            l1, l2, curr = curr, l1, 0
        return l1
        
        # BackTrack - 99 pass - Time Limit Exceeded
        """
        def backtrack(decoded, remaining, selected):
            if not remaining:
                #print(decoded)
                if str(decoded) not in selected:
                    selected.add(str(decoded))
                return selected
            for i in range(1,3):
                nxt = "".join(remaining[:i])
                if nxt and nxt[0] != "0" and (0 < int(nxt) < 27):
                    backtrack(decoded + [nxt], remaining[i:], selected)
            return selected
            
        return len(backtrack([], list(s), set()))
        """
        
        # GIST
        """
        # * Lesson: it looks like recursive should work here. Below naive does not work
        s = list(s)
        result = [""]
        for i in range(len(s)):
            one_letter = 96+int(s[i])
            if one_letter >= 97:
                if result:
                    result[0] += chr(one_letter)
            else:
                if result:
                    result.pop(0)
            if i+1 < len(s):
                two_letter = int(s[i]+s[i+1])
                if two_letter < 27 and len(str(two_letter)) == 2:
                    result.append(chr(two_letter))
        return len(result)
        """
        
