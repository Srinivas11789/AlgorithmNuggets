class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_units = 0
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for typ in boxTypes:
            if truckSize == 0:
                break
            for bx in range(1,typ[0]+1):
                if truckSize > 0 :
                    total_units += typ[1]
                    #print(total_units)
                    truckSize -=1
        return total_units
