#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#min() 함수 사용 금지

min_num = 10000
numbers = [0, 20, 100]

for i in numbers:
    if i < min_num:
        min_num = i

print(min_num)