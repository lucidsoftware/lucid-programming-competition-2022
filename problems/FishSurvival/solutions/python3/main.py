from sys import stdin, stdout

fish, events = map(int, stdin.readline().split())


for i in range(events):
    event, size = map(str, stdin.readline().split())
    if event == 'G':
        fish += int(size)
    else:
        fish = fish - fish%int(size)

stdout.write(str(fish))
stdout.flush()