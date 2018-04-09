# Enter your code here. Read input from STDIN. Print output to STDOUT


def testSplit(n, m, prices, charge):
    n = len(prices)
    total_shared = 0
    for i in range(n):
        if i == int(m):
            pass
        else:
            total_shared += int(prices[i])
    her_share = total_shared//2
    if her_share == int(charge):
        return "Bon Appetit"
    else:
        return int(charge) - her_share

# Main logic -  custom
def main():
    n, m = raw_input().strip().split(" ")
    prices = raw_input().split(" ")
    charge = raw_input()
    print testSplit(n,m,prices,charge)

main()
