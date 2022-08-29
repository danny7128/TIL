
T = int(input())
for j in range(1,T+1):
    N = int(input())
    value_ = []
    A = list(map(int, input().split()))
    A_dic = {}

    for i in A:
        if i not in A_dic:
            A_dic[i] = 1
        else:
            A_dic[i] += 1

    for key in A_dic:
        value_.append(A_dic[key])
    max_value = max(value_)     # 4
    max_index = value_.index(max_value)                            # 8을 찾아가면 된다
    A_key = list(A_dic)
    result_ = A_key[max_index]
    print(f'#{N} {result_}')

