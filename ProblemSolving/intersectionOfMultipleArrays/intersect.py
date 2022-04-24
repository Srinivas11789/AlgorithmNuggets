class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        intersection_logic = {}
        sorted_intersection = []
        
        for n in nums:
            
            for k in range(len(n)):
            
                if n[k] not in intersection_logic:
                    intersection_logic[n[k]] = 0
                intersection_logic[n[k]] += 1

                if intersection_logic[n[k]] == len(nums):
                    if not sorted_intersection:
                        sorted_intersection = [n[k]]
                    else:
                        for i in range(len(sorted_intersection)):
                            if i == len(sorted_intersection)-1 and sorted_intersection[i] < n[k]:
                                sorted_intersection.append(n[k])
                                break
                            elif n[k] < sorted_intersection[i]:
                                sorted_intersection = sorted_intersection[:i] + [n[k]] +sorted_intersection[i:]
                                break
                            
            print(sorted_intersection,intersection_logic)
            
        return sorted_intersection
