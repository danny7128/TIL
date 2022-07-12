#1부터 n까지의 곱을 구하여 출력하는 코드를
# 1) while 문 2) for 문으로 각각 작성하시오.

n = 5
m = 1
i = 1
while i <= n:
    m *= i
    i += 1
print(m)

m = 1
for j in range(1, n+1):
    m *= j
print(m)



# n = 5
# 120