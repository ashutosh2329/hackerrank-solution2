#!/bin/python3

import math
import os
import random
import re
import sys
# def reverse(n):
#     num = 0
#     while(n>0):
#         num =(num*10)+n%10
#         n = n//10
#     return num
def beautifulDays(i, j, k):
    c = 0
    for a in range(i,j+1):
         if (a - int(str(a)[::-1])) % k == 0:
        # if(abs(a-reverse(a))%k == 0):this can also be used for this uncomment the above method
            c += 1

    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
