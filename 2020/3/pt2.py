#!/bin/python

slope = []
with open('input.txt') as f:
    for line in f:
        slope.append(line[0:len(line) - 1])

# right 1 down 1
r1d1 = 0
right = 0
for line in slope:
    if line[right % len(line)] == '#':
        r1d1 += 1
    right += 1
print(r1d1)

# right 3 down 1
r3d1 = 0
right = 0
for line in slope:
    if line[right % len(line)] == '#':
        r3d1 += 1
    right += 3
print(r3d1)

# right 5 down 1
r5d1 = 0
right = 0
for line in slope:
    if line[right % len(line)] == '#':
        r5d1 += 1
    right += 5
print(r5d1)

# right 7 down 1
r7d1 = 0
right = 0
for line in slope:
    if line[right % len(line)] == '#':
        r7d1 += 1
    right += 7
print(r7d1)

# right 1 down 2
r1d2 = 0
right = 0
for line_num in range(0, len(slope)):
    if line_num % 2 == 1:
        continue
    if slope[line_num][right % len(line)] == '#':
        r1d2 += 1
    right += 1
print(r1d2)

print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)
