import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snake_board(n, apples, moves):
    board = [[0] * n for _ in range(n)]

    for ax, ay in apples:
        board[ax-1][ay-1] = 1

    move_info = {}
    for t, d in moves:
        move_info[t] = d

    time = 0
    direction = 0
    snake = deque([(0, 0)])
    board[0][0] = 2

    while True:
        time += 1

        head_x, head_y = snake[-1]
        nx, ny = head_x + dx[direction], head_y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            return time
        
        if board[nx][ny] == 0:
            tail_x, tail_y = snake.popleft()
            board[tail_x][tail_y] = 0

        snake.append((nx, ny))
        board[nx][ny] = 2
        
        if time in move_info:
                if move_info[time] == 'D':
                    direction = (direction + 1) % 4

                else:
                    direction = (direction - 1) % 4

n = int(input()) # N X N 보드 크기기
k = int(input()) #사과의 개수

apples = [] # 사과의 위치를 저장하는 리스트트

for _ in range(k):
    x, y = map(int, input().split())
    apples.append((x, y))

l = int(input())

moves = []

for _ in range(l):
    t, d = input().strip().split(" ")
    moves.append((int(t), d))

print(snake_board(n, apples, moves))
