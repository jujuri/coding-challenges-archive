import sys

input = sys.stdin.readline

s = input().strip()

ans = ""
tmp = ""
tag = ""
in_tag = False

for letter in s:
    if letter == "<":
        if len(tmp) > 0:
            ans += tmp[::-1]
            tmp = ""
        tag += letter
        in_tag = True
    elif letter == ">":
        tag += letter
        in_tag = False
        ans += tag
        tag = ""
    elif in_tag:
        tag += letter
    elif letter == " ":
        ans += tmp[::-1]
        ans += letter
        tmp = ""
    else:
        tmp += letter
ans += tmp[::-1]
    
print(ans)