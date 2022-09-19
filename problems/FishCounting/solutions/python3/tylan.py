from collections import Counter

s = Counter(input())

print('halibut:{}'.format(s['b']))
print('mackerel:{}'.format(s['k']))
print('salmon:{}'.format(s['o']))
print('snapper:{}'.format(s['p'] // 2))
print('squid:{}'.format(s['q']))
print('tuna:{}'.format(s['t'] - s['b']))