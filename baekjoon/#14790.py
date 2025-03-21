import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n, 0, -1):
        if str(j) == "".join(sorted(list(str(j)))):
            print(f"Case #{i+1}: {j}")
            break