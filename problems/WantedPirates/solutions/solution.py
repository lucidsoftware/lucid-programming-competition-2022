import sys

# parsing
num_lines = input()

lists = []
smallest = set()
for i in range(num_lines):
    line = input().split(',')
    country = line[0] # not actually important!
    pirates = set(line[1:])
    if len(pirates) < smallest:
        smallest = set(pirates)
    lists.append(pirates)

# algorithm O(number of countries * smallest list size)
for pirates in lists:
    for pirate in smallest:
        # only the contents of the already smallest list actually matter
        # because by definition if a pirate is not in the smallest list,
        # its not in every list
        # there may, however be multiple lists of smallest length
        # that have different pirates in them, so we still need to check
        if pirate not in pirates:
            pirates.remove(pirate)
    

# output
for pirate in sorted(smallest):
    print(pirate)



