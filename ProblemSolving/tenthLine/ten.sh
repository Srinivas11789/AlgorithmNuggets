# Read from the file file.txt and output the tenth line to stdout.

# Using sed - 100 pass
#sed -n 10p "file.txt"

# Using awk - 100 pass
# NR is the current row number. awk prints by default
awk "NR == 10" file.txt


