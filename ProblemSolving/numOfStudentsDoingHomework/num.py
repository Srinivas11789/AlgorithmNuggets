# Logic 1: Iterate both array together - 94% faster
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        student = 0
        count = 0
        while student < len(startTime):
            if startTime[student] <= queryTime <= endTime[student]:
                count += 1
            student += 1
        return count
