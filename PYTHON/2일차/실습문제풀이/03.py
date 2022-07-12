#1부터 n까지의 합을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.
#sum() 함수 사용 금지

n = int(input())
m = 0
num = 0
while m < n :
    m += 1
    num += m     
print(num)

# n = 10
# 55

n = int(input())
m = 0
num = 0

for m in range(n+1):
    num += m
print(num)