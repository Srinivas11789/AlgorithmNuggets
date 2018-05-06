class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        
        # Works - but a scale cases of [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
#[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612] fails the logic with memory error
        # Logic - For every heater placement add the heater it covers and check whether its equal to all the house array, try with radius 1 and ....
        covered = []
        n1 = len(houses)
        n = houses[n1-1]
        h = len(heaters)
        for radius in range(1,n):
            for h in heaters:
                covered.append(h)
                if h-radius > 0 and h-radius < n:# and h-radius not in covered:
                    covered.append(h-radius)
                if h+radius < houses:# and h+radius not in covered:
                    covered.append(h+radius)
            if len(set(covered)) == n:
                print covered
                return radius
        return -1
        
        
        
        
