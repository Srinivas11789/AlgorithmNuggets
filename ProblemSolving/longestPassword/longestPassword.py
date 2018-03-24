# Codility LongestPassword - 90 percent
# Failed for this case: asdf! 3ab qqqq adw3 - It seems that password should contain both the letters and numbers, the logic written was working for both letter and numbers only and together
# Above case, program gave 4 but expected was 3

# Changed the logic to have both the letters and numbers in the password but now fails for presence of '0'
# Codility LongestPassword
#

# Got it 0 is considered to be even, so changing the logic to get 90 percent pass

# Codility LongestPassword
# 
def solution(S):
    maxi = 0
    passwords = S.split(" ")
    for p in passwords:
        nums = 0
        alps = 0
        nvalid = ""
        avalid = ""
        for c in p:
            if ord(c) > 47 and ord(c) < 58:
                nums += 1
            elif ord(c) > 64 and ord(c) < 123:
                alps += 1
            else:
                nums = -1
                alps = -1
                nvalid = "False"
                avalid = "False"
                break
        if (nums > 0 and nums%2 != 0):
            nvalid = "True"
        else:
            nvalid = "False"
        if (alps >= 0 and alps%2 == 0):
            avalid = "True"
        else:
            avalid = "False"
        if nums == 0:
            nvalid = "False"
        #if alps == 0:
        #    avalid = "False"
        if (nvalid == "True" and avalid == "True") or (nvalid == "True" and avalid == "") or nvalid == "" and avalid == "True":
            if len(p) > maxi:
                maxi = len(p)
        if maxi == 0:
            maxi = -1
        #print(nvalid, avalid)
    return maxi

#############################################################
 
def solution(S):
    maxi = 0
    passwords = S.split(" ")
    for p in passwords:
        nums = 0
        alps = 0
        nvalid = ""
        avalid = ""
        for c in p:
            if ord(c) > 47 and ord(c) < 58:
                nums += 1
            elif ord(c) > 64 and ord(c) < 123:
                alps += 1
            else:
                nums = -1
                alps = -1
                nvalid = "False"
                avalid = "False"
                break
        if (nums > 0 and nums%2 != 0):
            nvalid = "True"
        else:
            nvalid = "False"
        if (alps > 0 and alps%2 == 0):
            avalid = "True"
        else:
            avalid = "False"
        if nums == 0:
            nvalid = "False"
        if alps == 0:
            avalid = "False"
        if (nvalid == "True" and avalid == "True") or (nvalid == "True" and avalid == "") or nvalid == "" and avalid == "True":
            if len(p) > maxi:
                maxi = len(p)
        if maxi == 0:
            maxi = -1
        #print(nvalid, avalid)
    return maxi
                

def solution(S):
    maxi = 0
    passwords = S.split(" ")
    for p in passwords:
        nums = 0
        alps = 0
        nvalid = ""
        avalid = ""
        for c in p:
            if ord(c) > 47 and ord(c) < 58:
                nums += 1
            elif ord(c) > 64 and ord(c) < 123:
                alps += 1
            else:
                nums = -1
                alps = -1
                nvalid = "False"
                avalid = "False"
                break
        if (nums > 0 and nums%2 != 0):
            nvalid = "True"
        else:
            nvalid = "False"
        if (alps > 0 and alps%2 == 0):
            avalid = "True"
        else:
            avalid = "False"
        if nums == 0:
            nvalid = ""
        if alps == 0:
            avalid = ""
        if (nvalid == "True" and avalid == "True") or (nvalid == "True" and avalid == "") or nvalid == "" and avalid == "True":
            if len(p) > maxi:
                maxi = len(p)
        if maxi == 0:
            maxi = -1
        #print(nvalid, avalid)
    return maxi
                
