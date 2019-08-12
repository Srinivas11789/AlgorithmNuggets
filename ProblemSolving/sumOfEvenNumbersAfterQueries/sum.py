class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        # Logic 1: Literally following the instructions in the problem - 73% faster
        # * Use filter to filter array of even numbers - but using filter for each iteration will make time limit exceeded
		# Logic translatable in any language
        
        # Number of queries
        n = len(queries)
        
        # Sum of all even numbers 
        sum_of_even_numbers = sum(filter(lambda x: x%2 == 0, A))
        
        # Result array storing query answers
        ans_for_query = [0]*n
        
        # Iteration of O(N) along the queries
        for i in range(n):
            
            # Value and Index of each query
            value = queries[i][0]
            index = queries[i][1]
            
            # Original value - If it was even lets remove it so we can add newly calculated value
            original_value = A[index]
            if original_value%2 == 0:
                sum_of_even_numbers -= original_value
                
            # New value based on the query - Also new value affecting the sum when even
            A[index] += value
            if A[index]%2 == 0:
                ans_for_query[i] = sum_of_even_numbers + A[index]
            else:
                ans_for_query[i] = sum_of_even_numbers
            
            # New sum of even numbers affected by the query
            sum_of_even_numbers = ans_for_query[i]
            
        return ans_for_query
