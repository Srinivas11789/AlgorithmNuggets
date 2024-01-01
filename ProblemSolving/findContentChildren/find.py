class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort(reverse=True)
        s.sort(reverse=True)

        count = 0
        for i in range(len(g)):
            if not s:
                return count
            if g[i] <= s[0]:
                s.pop(0)
                count += 1
        return count
