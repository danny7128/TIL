import sys

sys.stdin = open("BOJ_25304.txt")

X = int(input())        # 적힌 총 금액
N = int(input())        # 물건의 종류의 수
sum_list = []
result_ = 0

for i in range(N):
    a, b = map(int, input().split())
    sum_list.append(a * b)

result_ = sum(sum_list)

if result_ == X:
    print('Yes')
else:
    print('No')