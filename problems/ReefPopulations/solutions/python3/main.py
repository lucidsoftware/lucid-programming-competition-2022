from sys import stdin, stdout

n, q = map(int, stdin.readline().split())
reef = [0] + list(map(int, stdin.readline().split()))

for i in range(2, n+1):
    reef[i] ^= reef[i-1]

for _ in range(q):
    x, y = map(int, stdin.readline().split())
    stdout.write('{}\n'.format(reef[y] ^ reef[x-1]))

stdout.flush()