n, q = map(int, input().split())
reef = [0]
reef.extend(map(int, input().split()))

for i in range(2, n+1):
    reef[i] ^= reef[i-1]

for _ in range(q):
    x, y = map(int, input().split())
    print(reef[y] ^ reef[x-1])