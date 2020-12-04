#!/bin/python

with open('input.txt') as f:
    trees_encountered = 0
    distance = 0
    for line in f:
        if line[distance % (len(line) - 1)] == '#':
            trees_encountered += 1
        distance += 3
    print(trees_encountered)
