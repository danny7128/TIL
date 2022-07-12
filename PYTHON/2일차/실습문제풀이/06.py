# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

max_num = -10000
numbers = [0, 20, 100]

for i in numbers:
    if i >= max_num:
        max_num = i

print(max_num)

