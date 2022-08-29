import sys

sys.stdin = open("BOJ_17388.txt")

S, K, H = map(int, input().split())     # 숭실,고려,한양대학교 참여도 입력

sum_ = sum([S, K, H])                   # 참여도의 합

if sum_ >=100:                          # 참여도가 100이상이면
    print('OK')

else:                                   # 참여도가 100이상이 아닐때
    min(S, K, H)                        # 가장 작은 수 
    if S == min(S, K, H):               # 숭실 대학교가 가장 작으면
        print('Soongsil')
    elif K == min(S, K, H):             # 고려 대학교가 가장 작으면
        print('Korea')
    elif H == min(S, K, H):             # 한양 대학교가 가장 작으면
        print('Hanyang')
