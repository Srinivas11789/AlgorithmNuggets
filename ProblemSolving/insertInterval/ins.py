class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def isOverlapped(int1, int2):
            if int2[0] <= int1[0] <= int2[1] or int2[0] <= int1[1] <= int2[1]:
                return True
            elif int1[0] <= int2[0] <= int1[1] or int1[0] <= int2[1] <= int1[1]:
                return True
            return False
        
        overLappedIntervals = []
        resultingIntervals = []
        while intervals:
            curr = intervals.pop(0)
            left = curr[0]
            right = curr[1]
            if newInterval and isOverlapped(curr, newInterval):
                overLappedIntervals.append(curr)
                continue
            if overLappedIntervals:
                intervals = [curr] + intervals
                break
            if newInterval and newInterval[1] < curr[0]:
                resultingIntervals.append(newInterval) 
                newInterval = []
            resultingIntervals.append(curr)
        
        if overLappedIntervals:
            l = min(overLappedIntervals[0][0], newInterval[0])
            r = max(overLappedIntervals[-1][1], newInterval[1])
            resultingIntervals.append([l,r])
            resultingIntervals.extend(intervals)
            return resultingIntervals

        if newInterval:
            resultingIntervals.append(newInterval)

        return resultingIntervals
