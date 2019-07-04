class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        # Logic 1: 100 pass - 30% faster and 100% memory - Simple iteration to distribute candies 
        # * Got into a confusion where I though n increases for every iteration ( read the problem carefully )
        output = [0]*num_people
        i = 0
        iteration = 0
        n = candies
        
        while i < len(output) and candies:
            amount = len(output)*iteration + i + 1
            #print candies, amount
            if amount <= candies:
                output[i] += amount
                candies -= amount
            else:
                output[i] += candies
                candies = 0
            #print output, candies
            if i == len(output)-1:
                i = -1
                iteration += 1
            i += 1
        return output
