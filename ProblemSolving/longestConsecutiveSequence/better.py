class Solution:
    # 2*O(n) == O(n), add elements to memory and check for consecutive as we visit each one
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {} # can use set also
        maxi = 0
        for i in nums:
            visited[i] = True
        for i in nums:
            if i-1 in visited:
                continue
            current = i
            longest = 0
            while current in visited:
                longest += 1
                current += 1
            if longest > maxi:
                maxi = longest
        return maxi
            
