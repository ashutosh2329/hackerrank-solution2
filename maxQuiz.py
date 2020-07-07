#!/bin/python3

import math
import os
import random
import re
import sys

# returns value of max knowledge
def eva(s,d):
    c = 0
    for j in range(len(s)):
        if(s[j]=='1' or d[j]=='1'):
            c +=1
    return c
        
# The acmTeam function below.
def acmTeam(topic):
    d = 1
    lis = []
    lis1 = []
    for i in range(len(topic)-1):
        j=i+1
        while(j<len(topic)):
            lis.append(eva(topic[i],topic[j]))
            j +=1
    
    lis.sort(reverse=True)
    print(lis)
    for i in range(len(lis)):
        if(lis[i]==lis[i+1]):
            d +=1
        else:
            break
    
    lis1.append(lis[0])
    lis1.append(d)
    return lis1


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
