T = int(input())


for j in range(1,T+1):
    A = input()
    A_rev = A[::-1]
    A_rev_ = []
    print(f'#{j}',end = ' ')
    for i in A_rev:
        if i == 'q':
            print('p',end='')
        elif i == 'p':
            print('q',end='')
        elif i == 'b':
            print('d',end='')
        else:
            print('b',end='')
    print()