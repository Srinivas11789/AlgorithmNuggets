class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
      
        # Using itertools combinations - Short and easy logic - 100pass
        import itertools
        result = [list(nums)]
        
        # When the full array length is taken, we dont want combination where len== len(nums) hence reduced the iteration by 1
        
        for i in range(len(nums)):
            for comb in itertools.combinations(nums,i): # use permutation when order is important as in (2,1) != (1,2)
                # Sorted the nums in order to help eradiation duplicates
                result.append(sorted(comb))
        
        print result
        #return sorted(list(set(result)))
        #return list(set(sorted(result)))
        
        # Eradicating duplicates of list of list
        answer = []
        for item in result:
            if item not in answer:
                answer.append(item)
        return answer
        

