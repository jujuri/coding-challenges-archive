import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 0
    words = list(map(str, input().split()))
    
    for i in range(len(words)):
        if words[i] == "u" or words[i] == "ur":
            cnt += 10
        elif "lol" in words[i]:
            cnt += 10
        elif words[i] == "should"  or words[i] == "would":
            if i+1 < len(words):
                if words[i+1] == "of":
                    cnt += 10
    
    print(cnt)