input()
segs = [0] + [int(ea) for ea in input().split(' ')] + [0]

def checkDiff(x, y, arr):
    if x >= 0 and x < len(arr) and y >= 0 and y < len(arr):
        return abs(arr[y] - arr[x]) <= 4
    else:
        return True

stable = True
for i in range(len(segs)):
    stable = stable and all([checkDiff(i-3, i, segs), checkDiff(i-2, i, segs), checkDiff(i-1, i, segs),
                             checkDiff(i+1, i, segs), checkDiff(i+2, i, segs), checkDiff(i+3, i, segs)])

print(stable)
