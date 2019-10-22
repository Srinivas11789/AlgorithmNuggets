class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # Logic 1: Recursive Traverse all the inputs
        
        def recurse(array, chosen, result, itera):
            print(array, chosen)
            if array == self.s:
                #self.mini = min(self.mini, itera)
                if itera < self.mini:
                    self.mini = itera
                    self.ans = chosen
                result.append(chosen)
                return
            elif itera > self.mini:
                return
            else:
                for i in range(2, len(array)+1):
                    recurse(array[:i][::-1]+array[i:], chosen+[i], result, itera+1)
        
        self.s = sorted(A)
        self.mini = len(A)+1
        self.ans = []
        result = []
        recurse(A, [], result, 0)
        return self.ans
