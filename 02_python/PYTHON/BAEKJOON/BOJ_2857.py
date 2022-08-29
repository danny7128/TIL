# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 

import sys

sys.stdin = open('BOJ_2857.txt')

return_ = 0

for i in range(1, 6):
    T = input()
    if 'FBI' in T:
        print(i, end = ' ')
        return_ = 1
    else:
        continue

if return_ == 0:
            print('HE GOT AWAY!')

