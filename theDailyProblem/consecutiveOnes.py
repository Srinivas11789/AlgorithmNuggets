"""
Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
  # Fill this in.

print longest_run(242)
# 4
"""

def consec_ones(num):
    bina = bin(num)[2:]
    """
    left = 0
    right = len(bina)-1
    while left < right:
        print(bin[left:right])
        if set(bin[left:right]) == set("1"):
           return right-left
        if bin[left] == "0":
           left += 1
        elif bin[right] == "0":
           right -= 1
        else:
    """
    maxi = 0
    temp = 0
    for i in range(len(bina)):
        if bina[i] == "1":
            temp += 1
        else:
            temp = 0
        maxi = max(temp, maxi)       
    return maxi

print(consec_ones(242))
