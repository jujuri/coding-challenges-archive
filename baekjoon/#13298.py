import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    solutions = []

    for x in range(1, lt // l1 + 1):
        if (lt - l1 * x) % l2 == 0:
            y = (lt - l1 * x) // l2
            if y > 0 and a1 * x + a2 * y == at:
                solutions.append([x, y])

    if len(solutions) == 1:
        print(f"{solutions[0][0]} {solutions[0][1]}")
    else:
        print("?")