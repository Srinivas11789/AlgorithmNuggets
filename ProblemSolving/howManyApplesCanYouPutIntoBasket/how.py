class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # Logic to maximize the number of apples - 7% faster 100 pass
        # 1. Sort the weight of apples
        # 2. Remove the last apple (most weight) until weight is lesser than 5000
        arr.sort()
        left = 0
        right = len(arr)-1
        while left < right:
            if sum(arr[left:right+1]) < 5000: # Return as soon as you find the max num
                return right-left+1
            right -= 1
        return 0
    
        # This logic is to minimize the number of apples
        """
        basket = 3000
        arr.sort(reverse=True)
        apples = 0
        for w in arr:
            if basket-w < 0:
                continue
            else:
                basket -= w
                apples += 1
        return apples
        """

        """
         basket = []
        apples = sorted(arr)
        weight = 5000
        for apple in apples:
            if weight-apple > 0:
                basket.append(apple)
                weight -= apple
                #print(weight, apple)
            else:
                break
        return len(basket) 
        """
