import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cell = "*"
star = True
for i in range(n):
    if i == 0:
        cell = "*"
        star = True
    elif i % 2 == 0:
        cell = "*"
        star = True
    else:
        cell = "."
        star = False
    for j in range(m):
        if star:
            print("*", end="")
            star = False
        else:
            print(".", end="")
            star = True   
    print()