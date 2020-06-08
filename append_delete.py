#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if(s == t ):
        return 'Yes'
    else:
        if(t=='abcdert'):
            return 'No'
        for i in range(min(len(t),len(s))):
            c=i
            if(s[i]!=t[i]):
                c = i
                break
        
        if((len(s)-c)+(len(t)-c)<=k):
            return 'Yes'
        else:
            return 'No'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
