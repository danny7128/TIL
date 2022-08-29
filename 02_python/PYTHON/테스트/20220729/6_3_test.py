T = int(input())

for j in range(1,T+1):
    M = input()
    N_rep = M.replace('-','')
    N = list(map(int,N_rep))

    if N[0] == 3 or N[0] == 4 or N[0] == 5 or N[0] == 6 or N[0] == 9:
        print(f'#{j} 1')
    else:
        print(f'#{j} 0')
