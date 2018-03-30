#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    for i in range(len(grades)):
        if grades[i] >= 38:
            value = grades[i]//5 + 1
            if (value*5) - grades[i] < 3:
                grades[i] =  value*5
    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

