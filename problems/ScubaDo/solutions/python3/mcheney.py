# Does not work

toolNames = input().split(', ')
# print(toolNames)
toolNums = [int(ea) for ea in input().split(', ')]
tools = {}
for i in range(len(toolNames)):
    tools[toolNames[i]] = toolNums[i]
J = int(input())
canDo = []
for j in range(J):
    jName = input()
    jTools = input().split(', ')
    line = input().split(', ')
    jNums = [int(ea) for ea in line]
    if all([(jTools[i] in tools and tools[jTools[i]] >= jNums[i]) for i in range(len(jTools))]):
        canDo.append(jName)

print(*sorted(canDo), sep='\n')
