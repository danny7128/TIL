
value_ = []
A = 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
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
print(result_)

