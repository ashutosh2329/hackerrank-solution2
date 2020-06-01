#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    a.sort()
    lis =[2]
    for i in range(len(a)-1):
        c = 1
        for j in range(i+1,len(a)):
            if(a[j]-a[i]<=1):
                c += 1
            else:
                 break
        lis.append(c)
    return max(lis)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
