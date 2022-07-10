import math
import os
import random
import re
import sys
# Complete the 'kaprekarNumbers' function below.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
def kaprekarNumbers(p, q):
    # Write your code here
    arr = []
    for i in range(p, q+1):
        L = len(str(i))
        sq = str(i*i)
        r = int(sq[len(sq)-L:])
        l = sq[:len(sq)-L]
        if(l == ''):
            l = 0
        l = int(l)
        if(l+r == i):
            arr.append(i)
    if(len(arr) == 0):
        print('INVALID RANGE')
    else:
        print(' '.join(str(i) for i in arr))
    return 0
if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)