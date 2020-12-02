#!/bin/python

import re

valid = 0

for line in open('input.txt'):
    tokens = re.split('[- :]', line)
    first_occurence = int(tokens[0])
    second_occurence = int(tokens[1])
    char = tokens[2]
    password = tokens[4]
    first_location_matches = password[first_occurence - 1] == char
    second_location_matches = password[second_occurence - 1] == char
    if first_location_matches ^ second_location_matches:
        valid+=1
print(valid)
