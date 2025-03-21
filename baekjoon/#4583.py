import sys

input = sys.stdin.readline

while True:
    word = input().strip()
    result = ""
    printable = True
    if word == "#":
        break

    for letter in word:
        if letter == "b":
            result += "d"
        elif letter == "d":
            result += "b"
        elif letter == "p":
            result += "q"
        elif letter == "q":
            result += "p"
        elif letter in "iovwx":
            result += letter
        else:
            printable = False
            print("INVALID")
            break
    if printable:
        print(result[::-1])