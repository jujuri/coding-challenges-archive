import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())

numbers = list(map(int, input().split()))

cnt = 0
start = b%n-1

full_cycle_number = k // n

remainder = k % n 

sum = full_cycle_number * sum(numbers)

for i in range(remainder):
    sum += numbers[(start+i) % n]

print(sum)