import sys

sys.stdin = open("BOJ_5576.txt")

w_list = []
k_list = []

for _ in range(10):
    w_list.append(int(input()))

for _ in range(10):
    k_list.append(int(input()))

w_list.sort()
w_list = w_list[::-1]

k_list.sort()
k_list = k_list[::-1]

sum_w_list = sum(w_list[:3])
sum_k_list = sum(k_list[:3])

print(sum_w_list, sum_k_list)

