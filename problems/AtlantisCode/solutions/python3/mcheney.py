A = 'A'
B = 'B'
C = 'C'

input()
letters = input()

score = 0
abCount = 0
prev = None
for l in letters:
    if l == A:
        score += 1
    if l == B:
        if prev == A:
            score += 3  # equivelant of subtracting 1 for A and adding 4 for AB
            abCount += 1
        else:
            score += 2
    prev = l

score -= (letters.count(A + B)**2) * letters.count(C)

print(score)