# 1288. 새로운 불면증 치료법

import sys

sys.stdin = open('input_SWEA_9_1288.txt', 'r')

T = int(input())  

for i in range(1, T + 1):
    N = int(input())  
    cnt = 0
    result = []
    while True:
        cnt += 1  
        sheep = N * cnt 
        target = str(sheep)  
        digit = len(target)  
        for j in range(digit):
            if target[j] not in result:
                result.append(target[j]) 
        if len(result) == 10:
            break

    print('#{} {}'.format(i, cnt * N))

        



        






        

