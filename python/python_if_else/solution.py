#!/bin/python3

# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    remainder = n % 2
    if remainder != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
