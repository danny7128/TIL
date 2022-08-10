import sys

sys.stdin = open("BOJ_10101.txt")

list_tri = []
for _ in range(3):                                                                              # 세 각 입력
    list_tri.append(int(input()))

if list_tri[0] == list_tri[1] == list_tri[2]:                                                   # 세 각이 같으면 Equilateral
    print('Equilateral')
elif sum(list_tri) == 180:                                                                      # 세 각의 합이 같을 때
    if list_tri[0] == list_tri[1] or list_tri[0] == list_tri[2] or list_tri[1] == list_tri[2]:  # 두 각이 같으면 Isosceles
        print('Isosceles')
    elif list_tri[0] != list_tri[1] != list_tri[2]:                                             # 세 각이 각자 다르면 Scalene
        print('Scalene')

elif sum(list_tri) != 180:                                                                      # 세 각의 합이 180이 아니면 Error
    print('Error')