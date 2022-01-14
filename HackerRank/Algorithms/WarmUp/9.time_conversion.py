"""
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = ""
    #store the time in HH MM SS midday
    HH,MM,SS = s.split(":")
    midday = SS[2:]
    SS = SS[:2]
    
    #making into string to intiger
    HH = int(HH)
    
    #working on PM time
    if midday == "PM":
        #case I : just remove midday part from time if HH = 12
        if HH == 12:
            time = str(HH) + ":" + str(MM) + ":" + str(SS)
        else:
            #case II : increase hour from 12 and remove midday if HH not 12
            HH += 12
            time = str(HH) + ":" + str(MM) + ":" + str(SS)
            
    # working on AM time
    if midday == "AM":
        #case I : if HH is 12 make it 0 and remove midday and add extra 0 as string
        if HH == 12:
            HH = 0
            time = "0" + str(HH) + ":" + str(MM) + ":" + str(SS)
        #case II : if HH is not 12, remove midday and print as it is but add extra 0 if its single digit
        else:
            if HH >= 1 and HH <= 9:
                time = "0" + str(HH) + ":" + str(MM) + ":" + str(SS)
            else:
                time = str(HH) + ":" + str(MM) + ":" + str(SS)
    
    return time

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
