# Day 3 Program

# Full Cloth (a 2D array) global declaration (for example use 10x10, for input 1000x1000) 

## Do not use [["."]*10]*10 it is copies of the same list (mutations permitted everywhere)
field = [["."]*1000 for _ in range(1000)]

# To hold the data of all the ids
records = {}

def debug(field):
    """Print the full cloth with all entries"""
    for f in field:
        print "".join(f)

def construct(input):
    """Fill in Record with Id details and Fill in cloth, measure the overlap"""

    # Part1 output
    count = 0

    # Part2 output
    selected_id = ""
    count1 = 0 # Control for part 2 item

    # Iterate over the inputs
    for entry in input:
        if entry:
            # Construct the dictionary of records, for each entry
            entry = entry.split(" ")
            id = entry[0].strip("#")
            if id not in records:
                records[id] = {}
            try:
                records[id]["left"], records[id]["top"] = entry[2].strip(":").split(",")
                records[id]["width"], records[id]["height"] = entry[3].split("x")
            except:
                print entry
                print "Failed due to the above input!"

            if "indexes" not in records[id]:
                records[id]["indexes"] = []

            # Draw the rectangle in the region of the field declared above
            # construct indexes
            horizontal_index = [int(records[id]["left"]), int(records[id]["width"])]
            vertical_index = [int(records[id]["top"]), int(records[id]["height"])]
            #print horizontal_index, vertical_index
            while vertical_index[1]:
                  i = horizontal_index[0]
                  j = horizontal_index[1]
                  while j:
                      records[id]["indexes"].append([vertical_index[0], i])
                      if field[vertical_index[0]][i] == ".":
                         field[vertical_index[0]][i] = id
                      else:
                         if field[vertical_index[0]][i] == "X":
                            pass
                         else:
                             field[vertical_index[0]][i] = "X"
                             count += 1
                      i += 1
                      j -= 1
                  vertical_index[0] += 1
                  vertical_index[1] -= 1

    # Print the full cloth
    #debug(field)

    # Part 2 Calculation
    for id, vals in records.items():
        count1 = 0
        for index in vals["indexes"]:
            if field[index[0]][index[1]] != "X":
                count1 += 1
        if count1 == len(vals["indexes"]):
            selected_id = id

    return count, selected_id
        

def main():
    # Fetch input from url
    import requests, sys
    # Sent the cookie set through the environment variable to get this
    #input = requests.get("https://adventofcode.com/2018/day/8/input")

    # Hard Coded inputs
    input = open("31.input","r").read()
    input = input.split("\n")
    count, id = construct(input[:-1])
    print "Day 3: Part 1 answer is --> " + str(count)
    print "Day 3: Part 2 answer is --> " + id

main()
