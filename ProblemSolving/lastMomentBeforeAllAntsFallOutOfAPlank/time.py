class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        last = first = -1
        if left:
            last = max(left)
        if right:
            first = min(right)
        if last == -1:
            return n-first
        if first == -1:
            return last

        move = 0
        for i in range(n):
            last -= 1
            first += 1
            if last < 0 and first > n:
                return move
            move += 1
        
        return move
