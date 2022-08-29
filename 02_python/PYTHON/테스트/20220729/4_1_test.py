T = int(input())

for j in range(1,T+1):
    dic_ = {}
    N = map(int,input().split())
    for i in N:
        if i not in dic_:
            dic_[i] = 1
        else:
            dic_[i] += 1

    list_dic = list(dic_)
    for i in list_dic:
        if dic_[i] == 2:
            continue
        else:
            print(f'#{j} {i}')
