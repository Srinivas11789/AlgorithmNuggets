# 100 percent pass
# Given
# S - String of names
# C - Company name

def solution(S, C):
    
    # Directory of names
    directory = []
    
    # Function to verify only for english lower case characters
    def english_verify(name):
        for char in name:
            if ord(char) > 96 and ord(char) < 123:
                pass
            else:
                return "False"
        return "True"
    
    # Lower case everything
    C = C.lower()
    company_check = "False"
    if english_verify(C) == "True":
        company_check = "True"
        
    # Name handle
    names = S.split(",")
    for name in names:
        # Make lower case
        name = name.lower()
        name_check = "False"
        
        # Split name by space
        fullname = name.split(" ")
        if fullname[0] == "":
            fullname = fullname[1:]
        
        # Firstname
        firstname = fullname[0]
        if english_verify(firstname) == "True":
            name_check = "True"
        
        # Last Name
        lastname = fullname[len(fullname)-1]
        lastname = "".join(lastname.split("-"))
        if english_verify(lastname) == "True":
            name_check = "True"
        
        # Middle Name
        if len(fullname) == 3:
            middlename = fullname[1]
            if english_verify(middlename) == "True":
                name_check = "True"

        
        # Check name for conditions
        if company_check == "True" and name_check == "True":
            if len(fullname) == 3:
                email = lastname+"_"+firstname[:1]+"_"+middlename[:1]+"@"+C+".com"
                i = 2
                while email in directory:
                    email = lastname+"_"+firstname[:1]+"_"+middlename[:1]+str(i)+"@"+C+".com"
                    i = i + 1
            else:
                email = lastname+"_"+firstname[:1]+"@"+C+".com"
                i = 2
                while email in directory:
                    email = lastname+"_"+firstname[:1]+str(i)+"@"+C+".com"
                    i = i + 1
            directory.append(email)
            
    # Result string generation
    result_string = ""
    for i in range(len(directory)-1):
        result_string += directory[i]+", "
    result_string += directory[len(directory)-1]    
    
    #print(result_string)
    return result_string
            
        
    

