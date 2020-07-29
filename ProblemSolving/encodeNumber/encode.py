# Logic 1: Binary of N+1 and remove left most 1 - 100 pass 77.5% faster
class Solution:
    def encode(self, num: int) -> str:
        num += 1
        b = bin(num)[2:]
        return "1".join(b.split("1")[1:])
