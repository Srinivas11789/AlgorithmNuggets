# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        
        # Logic 1: 2 pointer method - 34% faster
        left = right = 0
        result = []
        while left < len(A) and right < len(B):
            if A[left][1] == B[right][1]:
                if A[left][0] < B[right][0]:
                    result.append(B[right][0:])
                else:
                    result.append(A[left][0:])
                left += 1
                right += 1
            elif A[left][1] > B[right][1]:
                if A[left][0] <= B[right][1]:
                    result.append([max(A[left][0],B[right][0]), B[right][1]])
                right += 1
            else:
                if B[right][0] <= A[left][1]:
                    result.append([max(A[left][0],B[right][0]), A[left][1]])
                left += 1
        return result
