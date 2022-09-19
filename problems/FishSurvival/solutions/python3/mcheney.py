F, E = [int(ea) for ea in input().split(' ')]

for e in range(E):
    line = input().split(' ')
    if line[0] == 'G':
        F += int(line[1])
    else:  # line[0] == 'P'
        F -= F % int(line[1])

print(F)
