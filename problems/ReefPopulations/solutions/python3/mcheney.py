# This solution might TLE

N, Q = [int(ea) for ea in input().split(' ')]
reef = [int(ea) for ea in input().split(' ')]

# make prefix XOR array
prefixArray = [reef[0]]
for ea in reef[1:]:
    prefixArray.append(prefixArray[-1] ^ ea)

for q in range(Q):
    x, y = [int(ea) - 1 for ea in input().split(' ')]
    if x > 0:
        print(prefixArray[y] ^ prefixArray[x-1])
    else:
        print(prefixArray[y])
