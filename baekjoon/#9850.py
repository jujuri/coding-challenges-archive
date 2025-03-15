import sys

input = sys.stdin.readline

enc_msg = input().strip()

for shift in  range(26):
    dec_msg = ""

    for char in enc_msg:
        if char.isalpha():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            dec_msg += new_char
        else:
            dec_msg += char
    if "CHIPMUNKS" in dec_msg and "LIVE" in dec_msg:
        print(dec_msg)
        break