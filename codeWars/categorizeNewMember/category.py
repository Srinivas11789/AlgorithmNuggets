def openOrSenior(data):
    result = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
