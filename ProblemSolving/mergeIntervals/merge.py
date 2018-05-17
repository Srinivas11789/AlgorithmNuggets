# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
	# 100 pass - Logic
        # Think in this manner - Corner Cases:
        # * when all the ranges come under the last range value
        # * Multiple varied range length spread across the array
        
        # Step1: Organize the array sorting with respect to the start range value, using key as start
        intervals = sorted(intervals, key=lambda t: t.start)
        
        # Result holding array
        result = []
        
        for ranges in intervals:
            # As the intervals are already sorted the first start will be first entry
            if not result:
                result.append(ranges)
            else:
                # As we know start is always sorted and the first entry will be the lowest, the end range is needed to be fixed
                # Access the last result to set the max range, this can be done by len(result)-1 or just -1
                if ranges.start <= result[-1].end:
                    result[-1].end = max(result[-1].end, ranges.end)
                else:
                    result.append(ranges)
        return result
            
        
        
        """
        # Sorting logic
        ranges = []
        result = []
        n = len(intervals)
        for i in range(n):
            ranges.append(intervals[i].start)
            ranges.append(intervals[i].end)
        ranges.sort()
        start = None
        for i in range(len(ranges)):
            if not start:
                start = i
            if ranges[i] > ranges[i-1]:
                result.append([start, i])
                start = None
        return result
        """
        
        
        """
        # Doesnt work for all entries clubbed to one range
        #ranges = []
        n = len(intervals)
        if n==1:
            return intervals
        i = 0
        while i < len(intervals)-1:
            new_range = Interval()
            print i, i+1
            if intervals[i+1].start <= intervals[i].end and intervals[i+1].end >= intervals[i].start:
                if intervals[i].start <= intervals[i+1].start:
                    new_range.start = intervals[i].start
                else:
                    new_range.start = intervals[i+1].start
                if intervals[i].end >= intervals[i+1].end:
                    new_range.end = intervals[i].end
                else:
                    new_range.end = intervals[i+1].end
                intervals[i] = new_range
                intervals.pop(i+1)
            else:
                new_range = intervals[i]
                intervals[i] = new_range
                #if i == n-2:
                #    ranges.append(intervals[i+1])
                i += 1
                
        return intervals
        """   
        
        """
        # ------> Not a Robust Logic
        ranges = []
        n = len(intervals)
        if n == 1:
            return intervals
        for i in range(1,n):
            if intervals[i].start in range(intervals[i-1].start,intervals[i-1].end+1): 
                rng = [intervals[i-1].start]
                if intervals[i].end >= intervals[i-1].end:
                     rng.append(intervals[i].end)
                else:
                     rng.append(intervals[i-1].end)
            elif intervals[i].start < intervals[i-1].start:
                rng = [intervals[i].start]
                if intervals[i].end >= intervals[i-1].end:
                     rng.append(intervals[i].end)
                else:
                     rng.append(intervals[i-1].end)
            else:
                #print ranges[len(ranges)-1][1], intervals[i-1].end
                if len(ranges) == 0:
                    ranges.append([intervals[i-1].start,intervals[i-1].end])
                if intervals[i-1].end != ranges[len(ranges)-1][1]:
                    ranges.append([intervals[i-1].start,intervals[i-1].end])
                rng = [intervals[i].start, intervals[i].end]
            ranges.append(rng)
        return ranges
        """
            
            
        
