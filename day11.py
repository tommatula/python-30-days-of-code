#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

maxSum = 0
for y in range(4):
    # do each y
    for x in range(4):
        # do each x
        curSum = 0
        curSum = curSum + arr[y][x]
        curSum = curSum + arr[y][x+1]
        curSum = curSum + arr[y][x+2]
        curSum = curSum + arr[y+1][x+1]
        curSum = curSum + arr[y+2][x]
        curSum = curSum + arr[y+2][x+1]
        curSum = curSum + arr[y+2][x+2]
        if curSum > maxSum or (x==0 and y==0):
            maxSum = curSum
print(maxSum)
