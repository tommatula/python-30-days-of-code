#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

#n = 10
count = 0
binaryStr = list()
while n >= 1:
    if n % 2 > 0:
        binaryStr.append('1')
    else:
        binaryStr.append('0')
    n = math.floor(n / 2)


count = 0
maxCount = 0
for i in binaryStr:
    if i == '1':
        count = count+1
    else:
        count = 0
    if count > maxCount:
        maxCount = count
        
print(maxCount)
