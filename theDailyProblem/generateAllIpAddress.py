"""
An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']
def ip_addresses(s, ip_parts=[]):
  # Fill this in.

print ip_addresses('1592551013')
# ['159.255.101.3', '159.255.10.13']
"""

# 

def ip_addresses(s, index, path, oct):
    if index == len(s)-1:
       result.append(path[:-1])
    for i in range(1, 4):
        #print(path, i, s[index:index+i])
        octet = path.split(".")
        print(path, index, i, octet, s[index:index+i])
        if oct < 4 and s[index:index+i] and s[index:index+i][0] != "0" and int(octet[-1] + s[index:index+i]) <= 255:
            ip_addresses(s, index+i, path+s[index:index+i]+"." , oct+1) 

result = []
ip_addresses('1592551013', 0, "", 0)
print(result)
# ['159.255.101.3', '159.255.10.13']


