class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        # Logic 1: Like literally solving by hand - 100 pass - longer run time...
        
        # First, Only if hand//W is a digit this should work
        # Hacky whole number division logic
        divided_parts = len(hand)/float(W)
        if ".0" not in str(divided_parts):
            return False
        
        # Second, make sure the list is sorted and remove consecutive numbers 
        result = []
        
        # Size of the each divided section, some scenarios have divided_parts != size_of_each_part
        size_of_each_part = len(hand)//int(divided_parts)
        
        # Iterate until hand remains
        while hand:
            # Set initials for every divided_parts 
            num = size_of_each_part # size of each part
            hand = sorted(hand) # make sure it is sorted
            result.append([]) # append to result list
            i = 0 # initialize i to start at beginning every time (scenario of repetitive elements)
            while num and i < len(hand):
                # Check for repetitive element
                if hand[i] not in result[-1]:
                    # Check for consecutive element
                    if result[-1] and result[-1][-1]+1 != hand[i]:
                        return False
                    result[-1].append(hand.pop(i))
                    num -= 1
                else:
                    # Case of repetitive element
                    i += 1
                    
        # Final result check
        if len(result) == int(divided_parts):
            return True
        else:
            return False
        
        """
        # Different approach ---pending...
        # Logic 2 - Using some shortcuts for a cleaner logic
        
        # By default we use the initial condition to beat unnecessary negative scenario cases
        
        # First, Only if hand//W is a digit this should work
        # Hacky whole number division logic
        division = len(hand)/float(W)
        if ".0" not in str(division):
            return False
        
        result = []
        # Size of each section that we divide
        quant = len(hand)//int(division)
        
        for i in range(int(division)):
            hand = set(hand)
            select = hand[:quant]
            if sum(select) != sum(range(select[0], select[quant])):
                return False
            result.append(select)
            hand = set(hand[quant:])
        """
            
            
            
                
            
        
        
