from sys import stdin, stdout
import copy


def get_direction(type):
    if type == "Land":
        return -1
    elif type == "Water North":
        return 0
    elif type == "Water South":
        return 1
    elif type == "Water East":
        return 2
    elif type == "Water West":
        return 3

def get_square_from_dir(w, h, dir, width, height):
    if dir == 0:
        if h == 0:
            return w,height-1
        return w,h-1
    elif dir == 1:
        if h == height-1:
            return w,0
        return w,h+1
    elif dir == 2:
        if w == width-1:
            return 0,h
        return w+1,h
    elif dir == 3:
        if w == 0:
            return width-1,h
        return w-1,h

def calculate_square(h, w, dir, odds, odds_list, dirs_list, width, height):
    type = dirs_list[h][w]
    if type == "Land":
        odds_list[h][w][dir] += odds
        return -1
    
    new_w, new_h = get_square_from_dir(w, h, dir, width, height)
    new_dir = get_direction(dirs_list[new_h][new_w])

    if new_dir == -1:
        odds_list[new_h][new_w][dir] += odds
    else:
        odds_list[new_h][new_w][dir] += odds/2
        odds_list[new_h][new_w][new_dir] += odds/2


    
hours = int(stdin.readline())
width, height = map(int, stdin.readline().split())

zeros = [[[0 for direction in range(4)] for col in range(width)] for row in range(height)]
cur_odds = copy.deepcopy(zeros)
next_odds = copy.deepcopy(zeros)
directions = [['' for col in range(width)] for row in range(height)]
for i in range(height):
    for j in range(width):
        directions[i][j] = stdin.readline().strip()
cur_odds[height//2][width//2][get_direction(directions[height//2][width//2])] = 100

for t in range(hours):
    for i in range(height):
        for j in range(width):
            for k in range(4):
                calculate_square(i,j,k,cur_odds[i][j][k], next_odds, directions, width, height)
    cur_odds = copy.deepcopy(next_odds)
    next_odds = copy.deepcopy(zeros)

total_odds = 0
for i in range(height):
    for j in range(width):
        if get_direction(directions[i][j]) == -1:
            for k in range(4):
                total_odds += cur_odds[i][j][k]

total_odds_rounded = round(total_odds)
stdout.write(str(total_odds_rounded))
stdout.flush()
