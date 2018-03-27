import os
file = open('README_backup.md','w')
link = "https://github.com/Srinivas11789/AlgorithmNuggets/tree/master/ProblemSolving/"
root, dirs, files = os.walk("ProblemSolving").next()
for dir in dirs:
    file.write("* ["+dir+"] ("+(link+dir)+")\n")
    #print "* ["+dir+"] ("+(link+dir)+")"
file.close()
