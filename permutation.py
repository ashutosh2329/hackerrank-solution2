#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    lis=[]
    for i in range(1,len(p)+1):
        for j in range(len(p)):
            if(i==p[j]):
                for k in range(len(p)):
                    if(j+1==p[k]):
                        lis.append(k+1)
                        break
                break
    return lis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
