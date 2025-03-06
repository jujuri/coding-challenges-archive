import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    field[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < m and field[nx][ny] == 1:
                queue.append([nx,ny])
                field[nx][ny] = 0

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i,j)
                count += 1

    print(count)