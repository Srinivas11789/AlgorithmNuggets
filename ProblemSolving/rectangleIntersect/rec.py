# Enter your code here. Read input from STDIN. Print output to STDOUT

def rectOverlap(r1, r2):
    
    # -7 > -3 or 3 < -4 or 8 < -3 or 5 > 6
    #print r1[0], r2[2], r1[2], r2[0], r1[1],  r2[3], r1[3], r2[1]
    if (int(r1[0])  >  int(r2[2])) or  (int(r1[2]) <  int(r2[0]))  or (int(r1[1]) < int(r2[3])) or (int(r1[3]) > int(r2[1])):
        return "no overlap"
    else:
        return "overlap"
    
    
    
def main():
    #r1 = list(input())
    #r2 = list(input())
    #r1 = [0,1,1,0]
    #r2 = [1,1,2,0]
    #r1 = [0,1,3,0]
    #r2 = [3,0,2,0]
    r1 = raw_input().split(" ")
    r2 = raw_input().split(" ")
    #print r1, r2
    print rectOverlap(r1, r2)
    
main()
