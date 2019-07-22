def create_phone_number(n):
    #your code here
    phoneNumber = "("
    for i in range(len(n)):
        phoneNumber += str(n[i])
        if i == 2:
            phoneNumber += ") "
        elif i == 5:
            phoneNumber += "-"
    return phoneNumber
