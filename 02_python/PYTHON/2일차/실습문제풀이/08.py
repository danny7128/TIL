# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

max_num = -10000
numbers = [0, 20, 100]

for i in numbers:
    if i >= max_num:
        max_num = i

print(max_num)

numbers.remove(max_num)
max_num = -10000

for i in numbers:
    if i >= max_num:
        max_num = i

print(max_num)