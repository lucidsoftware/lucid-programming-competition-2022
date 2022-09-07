from sys import stdin, stdout

nums = stdin.readline().split()

fuel = int(nums[0])
for x,num in enumerate(nums):
	if fuel < 0:
		break;
	fuel = max(fuel,int(num))
	#don't take away from fuel on the last index
	if x != len(nums)-1:
		fuel-=1

if fuel >= 0:
	stdout.write('1')
else:
	stdout.write('0')

stdout.flush()
