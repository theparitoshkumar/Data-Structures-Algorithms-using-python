#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    round_grades = []
    
    for grade in grades:
        abc = grade // 5
        next_multiple_of_5 = (abc * 5) + 5
        if grade < 38:
            round_grades.append(grade)
        elif next_multiple_of_5 - grade < 3:
            round_grades.append(next_multiple_of_5)
        else:
            round_grades.append(grade)
    return round_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
