#!/bin/python

adapters = []
with open('input.txt') as file:
    for line in file:
        adapters.append(int(line))
adapters.sort()

jolt_1 = 0
jolt_3 = 1
last_adapter = 0
for adapter in adapters:
    if adapter - last_adapter == 1:
        jolt_1 += 1
    elif adapter - last_adapter == 3:
        jolt_3 += 1
    last_adapter = adapter

print(jolt_1 * jolt_3)