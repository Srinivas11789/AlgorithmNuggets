class Solution:
    def partitionString(self, s: str) -> int:
        
        window = {}
        partitions = [[]]
        for i in range(len(s)):
            if s[i] in window:
                window = {s[i]:True}
                partitions.append([s[i]])
            else:
                partitions[-1] += s[i]
                window[s[i]] = True
            
        print(partitions)
        return len(partitions)

