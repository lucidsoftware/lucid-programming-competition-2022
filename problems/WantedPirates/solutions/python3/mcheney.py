N = int(input())
line = input().split(',')
inEveryCountry = set(line[1:])
for n in range(1, N):
    line = input().split(',')
    inEveryCountry = inEveryCountry.intersection(set(line[1:]))
print(*sorted(inEveryCountry), sep='\n')
