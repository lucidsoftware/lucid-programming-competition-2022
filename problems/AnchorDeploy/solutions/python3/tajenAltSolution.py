from sys import stdin, stdout
import math

chain, inputs = map(int, stdin.readline().split())

total_area = math.pi*chain**2
reef_area = 0
rock_area = 0

for i in range(inputs):
    obstacle, x, y, r = map(str, stdin.readline().split())
    if obstacle == 'reef':
        reef_area += math.pi*float(r)**2
    else:
        rock_area += math.pi*float(r)**2

reef_odds = reef_area/total_area
rock_odds = rock_area/total_area

fail_odds = reef_odds + reef_odds*rock_odds + reef_odds*rock_odds**2 + rock_odds**3

stdout.write("%.3f" % fail_odds)
stdout.flush()