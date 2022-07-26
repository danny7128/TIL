# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 별의 줄(갯수)만큼 입력
T = int(input())
# 1 ~ T 만큼 반복
for i in range(1, T+1):
    # i의 값이 짝수인지 확인
    # i의 값이 홀수면 
    if i % 2 == 1:
        print('*' * i)
    else:
        print('*' * i)


