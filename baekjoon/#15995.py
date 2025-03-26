import sys

input = sys.stdin.readline

a, m = map(int, input().split())

# (ax - 1) % m = 0
x = 1

while True:
    if (a*x-1) % m == 0:
        print(x)
        break
    x += 1