# 2071.평균값 구하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    int_list = list(map(int,input().split()))
    a = sum(int_list)/(len(int_list))
    print(f"#{test_case} {round(a)}")