def reaction(string):
    lstr = list(string)
    i = 0
    while i < len(lstr):
        if i < len(lstr)-1:
           if lstr[i].islower():
              if lstr[i].upper() == lstr[i+1]:
                 del lstr[i]
                 del lstr[i]
                 i -= 1
              else:
                 i += 1
           elif lstr[i].isupper():
              if lstr[i].lower() == lstr[i+1]:
                 del lstr[i]
                 del lstr[i]
                 i -= 1
              else:
                 i += 1
           else:
              i += 1
        else:
           i += 1
    return "".join(lstr)

def remove_problems(arg_string):
    orig_string = arg_string[:]
    Ustr = list(set(orig_string))
    mini = 600000
    visited = []
    for ch in Ustr:
        if ch.lower() not in visited or ch.upper() not in visited:
            visited.append(ch.lower())
            visited.append(ch.upper())
            string = orig_string[:].replace(ch.upper(), "")
            string = string.replace(ch.lower(), "")
            #print string, ch
            if len(reaction(string)) < mini:
               mini = len(reaction(string.replace(ch.upper(), "")))
    return mini

def main():
    input = open("51.input","r").read()
    input = input.split("\n")
    for inp in input:
        if inp:
            print "Part1: " + str(len(reaction(inp)))
            print "Part2: " + str(remove_problems(inp))
main()
