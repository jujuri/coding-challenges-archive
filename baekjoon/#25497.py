import sys

input = sys.stdin.readline

n = int(input())

skills = input().strip()

cnt = 0
s_cnt = 0
l_cnt = 0

for skill in skills:
    if skill in "123456789":
        cnt += 1

    elif skill == "S":
        s_cnt += 1
    elif skill == "L":
        l_cnt += 1
    elif skill == "K":
        if s_cnt > 0:
            s_cnt -= 1
            cnt += 1
        else:
            break
    elif skill == "R":
        if l_cnt > 0:
            l_cnt -= 1
            cnt += 1
        else:
            break
print(cnt)