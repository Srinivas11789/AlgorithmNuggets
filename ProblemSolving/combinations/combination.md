
1) A bit hacky solution using inbuilt function `itertools`
```
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # Logic: Use Python Itertools - 120ms 99% faster.
        # * K numbers ==> repeat=2
        # * 1..N is the limit ==> range(1,n)
        
        import itertools
        result = []
        
        for comb in itertools.combinations(range(1,n+1), r=k):
            result.append(comb)
            
        return result
```

2) Same logic above implemented as a single line solution
```
return [comb for comb in itertools.combinations(range(1,n+1), r=k)]
```

3) Recursive with comments on why?
```
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        # This is the sole idea of a brute force solution: (particularly when k=2)
        
        # This would be the general brute force logic for k=2 ==> 2 for loops...
        # * K input will contain k for loops --> use recursive function to for loop k times...
        
        # Brute force solution - worst case sceanrio
        result = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    if sorted([i,j]) not in result:
                        result.append([i,j])
        return result
        """
        
        # 100 pass 756ms
        # Implementing the same brute force solution (reference to the logic above..)
        result = []
        
        # A loop to carry forward the array constructed and next index to operate
        def k_times_for_loops(temp_array, index):
            
            # debug
            #print temp_array
            
            # Recursive function: First create a decision when to exit...
            # what should be the result, return once you get the result
            if len(temp_array) >= k:
                    # Avoid duplicates and same element arrays
                    if sorted(temp_array) not in result and len(set(temp_array)) == k:
                        result.append(temp_array)
                    return
                
            # Recurse with for loop k times, add the current index to list and operate on next index
            for i in range(index, n+1):
                k_times_for_loops(temp_array+[i], i+1)
        
        # Function trigger
        k_times_for_loops([], 1)
        return result
```
