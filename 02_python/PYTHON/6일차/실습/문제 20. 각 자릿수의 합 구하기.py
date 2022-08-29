# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

a = int(input())
str_a = str(a)
sum = 0
for i in (str_a):
    sum += int(i)
print(sum)
