# 2050. 알파벳을 숫자로 변환
import sys
sys.stdin = open("input.txt", "r")

T = input()
for test_case in T:
    print(ord(test_case)-64,end = ' ')
