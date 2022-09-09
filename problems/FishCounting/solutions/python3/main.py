from sys import stdin, stdout

scrambledList = stdin.readline()
charDict = {}

for i in scrambledList:
    if i in charDict:
        charDict[i] += 1
    else:
        charDict[i] = 1

if 'b' in charDict:
    stdout.write(f"halibut:{charDict['b']}\n")
    charDict['t'] -= charDict['b']
else:
    stdout.write("halibut:0\n")

if 'k' in charDict:
    stdout.write(f"mackerel:{charDict['k']}\n")
else:
    stdout.write("mackerel:0\n")

if 'o' in charDict:
    stdout.write(f"salmon:{charDict['o']}\n")
else:
    stdout.write("salmon:0\n")

if 'p' in charDict:
    stdout.write(f"snapper:{charDict['p']//2}\n")
else:
    stdout.write("snapper:0\n")

if 'q' in charDict:
    stdout.write(f"squid:{charDict['q']}\n")
else:
    stdout.write("squid:0\n")

if 't' in charDict:
    stdout.write(f"tuna:{charDict['t']}\n")
else:
    stdout.write("tuna:0\n")


stdout.flush()
