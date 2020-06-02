#!/bin/python3

import math
import os
import random
import re
import sys



def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    mid = 0
    c = -1
    while( first<=last):
        mid = (first + last)//2
        if item_list[mid] == item :
            break
        elif(first==last):
            if(item<item_list[last]):
                return (mid+2)
            else:
                break
        else:
            if item < item_list[mid]:
                first = mid + 1
            else:
                last = mid - 1 

    return (mid+1)
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    lis = []
    #remove 
    scores = list(dict.fromkeys(scores))
    for i in range(len(alice)):
        lis.append(binary_search(scores,alice[i]))

    return lis
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
