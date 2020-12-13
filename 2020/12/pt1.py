#!/bin/python

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0 # east = 0, N = 270

    def move(self, direction, distance):
        if direction == 'N':
            self.y += distance
        elif direction == 'E':
            self.x += distance
        elif direction == 'S':
            self.y -= distance
        elif direction == 'W':
            self.x -= distance
        elif direction == 'F':
            if self.angle == 0:
                self.move('E', distance)
            elif self.angle == 90:
                self.move('S', distance)
            elif self.angle == 180:
                self.move('W', distance)
            elif self.angle == 270:
                self.move('N', distance)
    
    def rotate(self, direction, degrees):
        if direction == 'L':
            self.angle = (self.angle - degrees + 360) % 360
        elif direction == 'R':
            self.angle = (self.angle + degrees) % 360

ship = Ship()
with open('input.txt') as file:
    for line in file:
        line = line.strip()
        action = line[0]
        amount = int(line[1:])
        if action in ['N', 'E', 'S', 'W', 'F']:
            ship.move(action, amount)
        elif action in ['L', 'R']:
            ship.rotate(action, amount)
print(abs(ship.x) + abs(ship.y))
