signs = 0
for i in range(4):
    if 'true' in input():
        signs += 1
if signs >= 3:
    print('Wait for the storm to pass.')
else:
    print('Go fishing!')
