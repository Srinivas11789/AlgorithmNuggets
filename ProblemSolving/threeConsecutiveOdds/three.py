class Solution:
    # Logic 1: Three consecutive odd - lt easy - 100 pass - 90% faster
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_consec = 0
        for i in range(len(arr)):
            if arr[i]%2 != 0:
                odd_consec += 1
            else:
                odd_consec = 0
            if odd_consec == 3:
                return True
        return False
