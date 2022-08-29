# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 
# B를 만들 수 있다면, A와 B를 애너그램이라고 한다.
# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

import sys
sys.stdin = open('BOJ_6996.txt')

N = int(input())

for i in range(N):
    a, b = input().split()
    list_b = list(b)

    if len(a) == len(b):

        for j in range(len(a)):
            if a[j] in list_b:
                list_b.remove(a[j])
                if len(list_b) == 0:
                    print(f'{a} & {b} are anagrams.')
            else:
                print(f'{a} & {b} are NOT anagrams.')
                
    
    else:
        print(f'{a} & {b} are NOT anagrams.')