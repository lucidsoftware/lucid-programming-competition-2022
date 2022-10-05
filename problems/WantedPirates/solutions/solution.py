import sys

# parsing
num_lines = int(input())

lists = []
smallest = None
for i in range(num_lines):
    line = input().split(',')
    country = line[0]  # not actually important!
    pirates = set(line[1:])
    if not smallest or len(pirates) < len(smallest):
        smallest = pirates
    lists.append(pirates)

# algorithm O(number of countries * smallest list size)
for pirates in lists:
    toRemove = set()
    for pirate in smallest:
        # only the contents of the already smallest list actually matter
        # because by definition if a pirate is not in the smallest list,
        # its not in every list
        # there may, however be multiple lists of smallest length
        # that have different pirates in them, so we still need to check
        if pirate not in pirates:
            toRemove.add(pirate)
    smallest = smallest - toRemove
    

# output
for pirate in sorted(smallest):
    print(pirate)



