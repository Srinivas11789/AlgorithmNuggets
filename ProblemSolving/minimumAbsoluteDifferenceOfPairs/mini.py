class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        # Logic 2: Arrange consecutive or sorted and just calculate i, i+1 which will be most optimal choice for min - 100 pass 55% faster
        arr = sorted(arr)
        result = []
        mini = arr[1]-arr[0]
        for i in range(len(arr)-1):
            pair = [arr[i], arr[i+1]]
            if (arr[i+1]-arr[i]) < mini:
                mini = arr[i+1]-arr[i]
                result = [[arr[i],arr[i+1]]]
            elif (arr[i+1]-arr[i]) == mini:
                result.append([arr[i],arr[i+1]])
        return result
        
        # Logic 1: Naive Iteration without Sorted ( we might have to use merge sort instead of insertion ) - Fail! Obvious time limit exceeded!
        """
        result = []
        mini = float('inf')
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                pair = [arr[i], arr[j]]
                diff = abs(arr[i]-arr[j])
                ans = [min(pair), max(pair)]
                if diff < mini:
                        mini = diff
                        result = [ans]
                elif diff == mini:
                        k = 0
                        br = True
                        while k < len(result):
                            if ans[0] >= result[k][0]:
                                k += 1
                            else:
                                break
                        #print(result[:i] + [ans] + result[i:])
                        result = result[:k]+[ans]+result[k:]
        return result
        """
        
            
        
