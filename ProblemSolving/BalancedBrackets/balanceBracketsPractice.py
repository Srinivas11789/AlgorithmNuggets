def is_matched(expression):
    braces = []
    match = {'{':'}','[':']','(':')'}
    for bracket in expression:
        if bracket in match.keys():
            braces.append(bracket)
        if bracket in match.values():
            #print braces
            last = len(braces)
            if last > 0:
                if match[braces[last-1]] == bracket:
                    del braces[last-1]
                else:
                    return -1
            else:
                return -1
    if braces:
            return -1
    else:
            return 1
        
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

