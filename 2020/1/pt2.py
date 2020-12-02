#!/bin/python

nums = []
for line in open('input1.txt'):
    nums.append(int(line))

for x in nums:
    for y in nums:
        for z in nums:
            if x + y + z == 2020:
                print(x * y * z)
