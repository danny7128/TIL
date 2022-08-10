import sys

sys.stdin = open("BOJ_14467.txt")

N = int(input())
cnt = 0
list_ = [-1] * (N + 1)
# 밑에껀 실수
# for _ in range(N+1):
#     list_.append([-1])

for _ in range(N):
    i, j = map(int, input().split())

    if list_[i] == -1 :
        list_[i] = j
        
    else:
        if list_[i] != j:
            list_[i] = j
            cnt += 1


print(cnt)

    

