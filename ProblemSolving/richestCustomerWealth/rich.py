# Logic 1: Naive matrix row iteration and sum - 100 pass - 72% faster
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthy = 0
        wealthy_cust = -1
        for customer in range(len(accounts)):
            current_cust_wealth = sum(accounts[customer])
            if current_cust_wealth > wealthy:
                wealthy = current_cust_wealth
                wealthy_cust = customer
        return wealthy
