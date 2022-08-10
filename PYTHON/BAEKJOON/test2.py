import sys

sys.stdin = open("test.txt")

N_list = []

for _ in range(5):
    N_list.append(int(input()))

sum_N_list = sum(N_list)
avg_N_list = (sum_N_list // 5)
sord_N_list = sorted(N_list)
print(avg_N_list)
print(sord_N_list[2])