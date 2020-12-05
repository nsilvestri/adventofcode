#!/bin/python

with open('input.txt', 'r') as file:
    seats = []
    for line in file:
        binary_string = ''
        for char in line.strip():
            if char == 'B' or char == 'R':
                binary_string = binary_string + '1'
            else:
                binary_string = binary_string + '0'
        seats.append(int(binary_string, 2))
    seats = sorted(seats)
    for i in range(1, len(seats)):
        if seats[i] - seats[i - 1] > 1:
            print(str(seats[i]) + ' ' + str(seats[i - 1]))
        
# printed 1001111001
#         BFFBBBBLLR