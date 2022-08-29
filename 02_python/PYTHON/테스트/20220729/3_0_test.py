T = int(input())


for j in range(1,T+1):
    A = input()
    A_rev = A[::-1]
    A_rev_ = []
    for i in A_rev:
        if i == 'q':
            A_rev_ += 'p'
        elif i == 'p':
            A_rev_ += 'q'
        elif i == 'b':
            A_rev_ += 'd'
        else:
            A_rev_ += 'b'
    print(f'#{T}',end = ' ')

    for i in A_rev_:
        print(i ,end = '')

