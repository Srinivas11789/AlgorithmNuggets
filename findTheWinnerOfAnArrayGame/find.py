class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        consec = 0
        max_item = max(arr)
        first = arr.pop(0)
        if k > len(arr):
            return max_item
        while consec < k:
            oppo = arr.pop(0)
            if first >= oppo:
                arr.append(oppo)
                consec += 1
            else:
                consec = 1
                first = oppo
                arr.append(first)
            #print(first, arr, consec)
        return first

