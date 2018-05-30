# Consecutive Sums

def consecutiveSums(num):
    count = 0
    curr_sum = 0
    i = 0
    while i < num//2+2:
        cviurr_sum += i
        if curr_sum == num:
           curr_sum = 0
           count += 1
        elif curr_sum > num:
           curr_sum = 0
        else:
           i += 1
    return count

def main():
    num = 21
    print consecutiveSums(num)

main()
