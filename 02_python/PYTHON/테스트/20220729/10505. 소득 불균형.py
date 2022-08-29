T = int(input())
cnt = 0
cnt_sum = []


for i in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    avg_ = sum(A)/len(A)
    for j in A:
        if j <= avg_:
            cnt += 1
    print(f'#{i} {cnt}')
    cnt = 0




