class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # 1, 2, 3 stones could be taken at one turn. Based on the example if there is 4 stones then thereu is no possibility for you to win. 
        # Think of reducing any number to 4, you cannot win, but if it is more than 4 like 5,6,7 you can make it four to make sure you win for sure.
        # for 4,8,12 and other numbers divisible by four, you always end up at the point where there are 4 stones remaining hence you cannot win. Thus the logic!
        if n%4 == 0:
            return False
        else:
            return True
        
"""
# Explanation based on leetcode:
You can always win a Nim game if the number of stones nn in the pile is not divisible by 44.

Reasoning

Let us think of the small cases. It is clear that if there are only one, two, or three stones in the pile, and it is your turn, you can win the game by taking all of them. Like the problem description says, if there are exactly four stones in the pile, you will lose. Because no matter how many you take, you will leave some stones behind for your opponent to take and win the game. So in order to win, you have to ensure that you never reach the situation where there are exactly four stones on the pile on your turn.

Similarly, if there are five, six, or seven stones you can win by taking just enough to leave four stones for your opponent so that they lose. But if there are eight stones on the pile, you will inevitably lose, because regardless whether you pick one, two or three stones from the pile, your opponent can pick three, two or one stone to ensure that, again, four stones will be left to you on your turn.

It is obvious that the same pattern repeats itself for n=4,8,12,16,…, basically all multiples of 44.
"""
        
        
