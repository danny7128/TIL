
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b, c = list(map(int,input().split()))
print((a if (a< b) else b) if ((a if a<b else b)<c) else c)