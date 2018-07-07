class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        # Only 5 10 20 dollars based on the question
        # Variables holding the count of all the denominations
        five = 0
        ten = 0
        twenty = 0
        
        # Iterating the customer payment
        n = len(bills)
        for i in range(n):
            
            # Price of the lemonade is 5
            change = bills[i] - 5
            
            while change > 0:
                print bills[i], change, five, ten
                
                # Change containing 5 denomination
                if change%10 != 0 and change%5 == 0:
                    if five > 0:
                        change -= 5
                        five -= 1
                    else:
                        return False
                else:
                    # 20 doesnt matter, only 10 matters
                    if ten > 0:
                        change -= 10
                        ten -= 1
                    elif five > 0:
                        change -= 5
                        five -= 1
                    else:
                        return False
                    
            # Count Coins
            if bills[i] == 5:
                    five += 1
            elif bills[i] == 10:
                    ten += 1
            else:
                twenty += 1
            
        if change == 0:
                return True
        else:
                return False
                
        """
        # Logic for every denomination
        
        # Count everything
        n = len(bills)
        coins = {}
        for i in range(n):
            
            # Price of the lemonade is 5
            change = bills[i] - 5
            
            while change > 0:
                #print change, coins
                if change in coins and coins[change] > 0:
                    coins[change] -= 1
                    change -= change
                elif change%5 == 0 and change%10 != 0:
                    if 5 in coins and coins[5] > 0:
                        coins[5] -= 1
                        change -= 5
                    else:
                        return False
                else:
                    for k,v in coins.items():
                        if k <= change and v > 0:
                            change -= k
                            coins[k] -= 1
                            break
                            
            # Coins dictionary counting all the coins
            if bills[i] not in coins:
                coins[bills[i]] = 0
            coins[bills[i]] += 1
            
        if change == 0:
                return True
        else:
                return False
        """
        
        
        """
        # Scale case fail
        n5 = 0
        n = len(bills)
        for i in range(n):
            if bills[i] == 5:
                n5 += 1
            else:
                while bills[i] > 5:
                    bills[i] -= 5
                    n5 -= 1
                    if n5 < 0:
                        return False
                n5 += 1
        return True
        """

                    
        
