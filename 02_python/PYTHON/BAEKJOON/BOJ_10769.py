import sys

sys.stdin = open("BOJ_10769.txt")

T = input()

happy_cnt = T.count(':-)')
sad_cnt = T.count(':-(')


# print(happy_cnt, sad_cnt)


if  happy_cnt == 0 and sad_cnt == 0:
    print('none')
elif happy_cnt > sad_cnt:
    print('happy')
elif happy_cnt < sad_cnt:
    print('sad')
elif happy_cnt == sad_cnt:
    print('unsure')

