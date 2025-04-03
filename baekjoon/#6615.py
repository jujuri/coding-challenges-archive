import sys

input = sys.stdin.readline

def find_steps(n):
    steps = {}
    cnt = 0
    while n != 1:
        steps[n] = cnt
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1
    steps[1] = cnt
    return steps

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    sa = find_steps(a)
    sb = find_steps(b)
    common_numbers = set(sa.keys()) & set(sb.keys())
    first_meeting = min(common_numbers, key=lambda x: sa[x] + sb[x])

    print(f"{a} needs {sa[first_meeting]} steps, {b} needs {sb[first_meeting]} steps, they meet at {first_meeting}")