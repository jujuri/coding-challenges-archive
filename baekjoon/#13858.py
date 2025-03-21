import sys

input = sys.stdin.readline

k, pos = map(int, input().split())

rs = list(map(int, input().strip()))

for _ in range(k):
    new_rs = []
    for i in range(0, len(rs), 2):
        count = rs[i]
        number = rs[i+1]
        for _ in range(count):
            new_rs.append(number)
    rs = new_rs

print(rs[pos])