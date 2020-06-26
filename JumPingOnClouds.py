#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    e= 100
    while((i+k)%len(c)!=0):
        i=(i+k)%len(c)
        print(i)
        e-=1
        if(c[i]==1):
            e-=2
    
    if(c[0]==1):
        e-=2    
    return e-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
