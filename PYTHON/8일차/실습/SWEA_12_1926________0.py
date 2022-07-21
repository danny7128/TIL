# 1926. 간단한 369게임
import sys
sys.stdin = open("input_SWEA_12_1926.txt", "r")

j = []
k = []
T = int(input())
for test_case in range(1, T + 1):
    for i in str(test_case):
        j += i
    
    for k in j:
        if k == '3' or k == '6' or k == '9' :
            j = []
            j += ['-']
            
        else:
            continue
    print(j)
    j = []







    # if str(test_case) in ['3' ,'6', '9']:
    #     print('-')
    # else:
    #     print(test_case)
