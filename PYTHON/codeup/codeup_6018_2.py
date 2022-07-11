a = '1 2 3'
print(a.split())
# 문자열을 특정 단위로 쪼개줌!
# 리스트!
# ['1', '2', '3']
numbers = a.split()
result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(result)

