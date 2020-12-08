#!/bin/python

instructions = []
with open('input.txt') as file:
    for line in file:
        instructions.append(line.strip())

accumulator = 0
cur_instruction = 0
executed = set()

while cur_instruction not in executed:
    executed.add(cur_instruction)
    instr = instructions[cur_instruction]
    tokens = instr.split()

    if tokens[0] == 'jmp':
        cur_instruction += int(tokens[1])
        continue
    elif tokens[0] == 'acc':
        accumulator += int(tokens[1])
    elif tokens[0] == 'nop':
        pass
    cur_instruction += 1

print(accumulator)