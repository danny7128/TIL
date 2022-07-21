#1989. 초심자의 회문 검사

import sys
sys.stdin = open("input_SWEA_10_1989.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = input()
    a = a.strip()
    b = a[::-1]

    if a == b:
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")
