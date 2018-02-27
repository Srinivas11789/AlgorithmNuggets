#!/bin/python

import sys

def isBalanced(s):
    # Complete this function
    braces = {'{':'}','[':']','(':')'}
    brackets = [item for item in s]
    result = []
    """
    result = "YES"
    for i in range(len(brackets)-1,-1,-1):
        if brackets[i] in braces.keys():
            item = brackets[i]
            #print item,i
            if brackets[(len(brackets)-1)-i] != braces[item]:
                #print brackets[(len(brackets)-1)-i], braces[item]
                result = "NO"
    return result
    """
    for i in range(0,len(brackets)):
            #print result
            if brackets[i] in braces.keys():
                result.append(brackets[i])
            if brackets[i] in braces.values():
                result.append(brackets[i])
                #print result
                if len(result) >= 2:
                    if result[len(result)-2] in braces.keys():
                        if brackets[i] == braces[result[len(result)-2]]:
                            del result[len(result)-1]
                            del result[len(result)-1]
                #print result
                        
                """
                    if result:
                        open1 = result[len(result)-1]
                        if brackets[i] == braces[open1]:
                            del result[len(result)-1]
                """
    if not result:
        return "YES"
    else:
        return "NO"
        

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s)
        print result
