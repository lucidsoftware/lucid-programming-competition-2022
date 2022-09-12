#!/usr/bin/env python3

import re, sys

def parse_known_coordinate(line):
    match = re.match(r"^\((-?\d+),(-?\d+)\)$", line)
    x = int(match.group(1))
    y = int(match.group(2))
    return (x, y)

def parse_instruction(line):
    match = re.match(r"^Walk (north|south|east|west) (\d+) paces?$", line)
    direction = match.group(1)
    amount = int(match.group(2))
    if (direction == "north"):
        return (0, amount)
    elif (direction == "south"):
        return (0, -amount)
    elif (direction == "east"):
        return (amount, 0)
    else:
        return (-amount, 0)

lines = sys.stdin.readlines()

(x, y) = parse_known_coordinate(lines[1])

instructions = [parse_instruction(line) for line in lines[2:]]
sum = (0, 0)
[sum := (sum[0] + instruction[0], sum[1] + instruction[1]) for instruction in instructions]
(dx, dy) = sum

if (x != 0):
    result = x // dx
    print(result)
else:
    result = y // dy
    print(result)
