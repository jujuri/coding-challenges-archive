import sys

input = sys.stdin.readline

n = int(input())

room = [] 
cnt_horizontal = 0
cnt_vertical = 0

for _ in range(n):
    row = list(map(str, input().strip()))
    room.append(row)
    cnt = 0
    for seat in row:
        if seat == ".":
            cnt += 1
        elif seat == "X":
            cnt = 0
        if cnt == 2:
            cnt_horizontal += 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if room[j][i] == ".":
            cnt += 1
        elif room[j][i] == "X":
            cnt = 0
        if cnt == 2:
            cnt_vertical += 1

print(cnt_horizontal, cnt_vertical)