import sys

input = sys.stdin.readline

a, b = map(int, input().split())

if a//2 > b:
    print(b)
elif a < 2:
    print(0)
else:
    print(a//2)