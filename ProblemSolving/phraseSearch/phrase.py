# Phrase search in a string

def phraseSearch(string, phrase):
    
    string = string.split(" ")
    #print string
    phrase = phrase.split(" ")
    
    """ 
    # Pythonic approach
    if phrase in string:
       return "YES"
    else:
       return "NO"
    """

    """
    # Naive ON approach
    i = 0
    if phrase[i] in string:
            for j in range(string.index(phrase[i])+1,string.index(phrase[i])+len(phrase)):
                i += 1
                if  string[j].strip('.') == phrase[i]:
                    pass
                else:
                    return "NO"
            return "YES"
    """    

    # Dictionary approach
    # Order in which the phrase occurs??
 
    dic = {}
    for s in string:
        s = s.strip(".?,")
        if s not in dic:
           dic[s] = 0
        dic[s] += 1

    #print dic
   
    for p in phrase:
        if p in dic and dic[p] > 0:
           dic[p] -= 1
        else:
           return "NO"
    return "YES"
         
           


def main():
    string = "Hi how are you?, when is the cat out of the bag. Please let me know"
    print phraseSearch(string, "cat out of the bag")

main()
