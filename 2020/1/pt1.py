#!/bin/python

nums = []
for line in open('input1.txt'):
    nums.append(int(line))

nums.sort()

for n in nums:
    if 2020 - n in nums:
        print(n * (2020 - n))
