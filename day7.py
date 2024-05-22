#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

outPut = ''
i = len(arr)
for i in range(len(arr),0,-1):
    outPut = outPut + str(arr[i-1]) + " "
print(outPut)

