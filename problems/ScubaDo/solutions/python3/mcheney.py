# Does not work

toolNames = input().split(', ')
print(toolNames)
toolNums = [int(ea) for ea in input().split(', ')]
tools = {}
for i in range(len(toolNames)):
    tools[toolNames[i]] = toolNums[i]
print(tools)
J = int(input())
canDo = []
for j in range(J):
    jName = input()
    print(jName)
    jTools = input().split(', ')
    line = input().split(', ')
    # print(line)
    print(jTools)
    print(line)
    jNums = [int(ea) for ea in line]
    if all([(jTools[i] in tools and tools[jTools[i]] >= jNums[i]) for i in range(len(jTools))]):
        canDo.append(jName)

print(*sorted(canDo, key=lambda x: x.lower()), sep='\n')
