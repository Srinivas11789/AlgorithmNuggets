## TwoLists
# separate the array into 2 of size N with lowest and higest separate


def twoList(list1, N):
    list1 = sorted(list1)
    return list1[:N], list1[-N:]

def main():
    list1 = [-11,9,10,5,0,0.25]
    N = 4
    print twoList(list1, N)

main()
