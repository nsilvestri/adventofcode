#!/bin/python

import re

valid = 0

for line in open('input.txt'):
    tokens = re.split('[- :]', line)
    min_occurence = int(tokens[0])
    max_occurence = int(tokens[1])
    char = tokens[2]
    password = tokens[4]
    if password.count(char) >= min_occurence and password.count(char) <= max_occurence:
        valid+=1
print(valid)
