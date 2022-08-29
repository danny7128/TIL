T = int(input())
for j in range(1, T+1):
    A = list(map(int, input().split()))
    sum_ = 0
    list_1 = []
    list_2 = []

    for i in range(1,len(A)+1):
        if i % 2 == 1:      #홀수면 *2
            list_1.append(A[i-1]*2)
        else:
            list_2.append(A[i-1])

    list_sum = sum(list_1)+sum(list_2)
    M = (list_sum % 10)
    for i in range(0,10):
        if (i + M) %10 == 0:
            print(f'#{j} {i}')
