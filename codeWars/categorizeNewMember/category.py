# Logic 1
def openOrSenior(data):
    result = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

# Logic 2
def openOrSenior2(data):
    return ["Senior" if (age >= 55 and hcap > 7) else "Open" for age, hcap in data]


