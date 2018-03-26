### Cracking the coding interview Hackerrank - Tries: Contacts problem

# Similar to implementing a search engine type of search.
# * Inital methods of regex and list failed
# * Was wondering about the dictionary method to reduce the time complexity - 
# ** Can each character stored with the index in the dictionary and counted further?
# ** Can each sub string stored as a key in the dictionary? Like for hack, h: ha: hac: hack:
#    - this works 100 percent


#Logic 3 - Dictionary method
import re
n = int(raw_input().strip())
directory = {}
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    # Store each character or set of characters as key in dictionary
    #print directory
    if "add" in op:
        for i in range(1,len(contact)+1):
            # For a string split using index - every i return that much lenght of a string
            if contact[:i] not in directory:
                directory[contact[:i]] = 0
            directory[contact[:i]] += 1
    else:# "find" in op:
        if contact in directory:
            print directory[contact]
        else:
            print "0"
    """
    # Logic1: regular expression method
    # Regex method - Still timeout occurs
    # Some error and timeout
    directory = ""
    op, contact = raw_input().strip().split(' ')
    if "add" in op:
        directory = directory + " " + contact
    else:
        search = re.findall(contact, directory)
        print len(search)
    """

    """
    # Logic2: List method
    # No errors and timeout
    #directory = []
    # For loop logic - timeout errors
    op, contact = raw_input().strip().split(' ')
    if "add" in op:
        directory.append(contact)
    elif "find" in op:
        count = 0
        for word in directory:
            if contact in word:
                count += 1
        print count
    else:
        print "Invalid operation"
    """
        
        
        
        

