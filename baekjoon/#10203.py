import sys 

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    count = 0
    word = input().strip()
    for letter in word:
        if letter in "aeiou":
            count +=1
    print("The number of vowels in " + word + " is " + str(count) + ".")