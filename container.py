#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the organizingContainers function below.
def organizingContainers(container1,container2):
    pts = "Possible";
    container1.sort()
    container2.sort()
    print(container1)
    print(container2)
    for i in range(n):
        if(container1[i]!=container2[i]):
            pts = "Impossible"
            break

    return pts
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container1 = [0]*n
        container2 = [0]*n

        for i in range(n):
            x = input().split()
            for j in range(n):
                container1[i] +=int(x[j])
                container2[j] +=int(x[j])

        result = organizingContainers(container1,container2)

        fptr.write(result + '\n')

    fptr.close()

