# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 
# 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

word = [ 'a', 'e', 'i', 'o', 'u' , 'A', 'E' , 'I', 'O', 'U']

while True:
    list_ = []
    sum_ = 0

    T = input()

    if T == '#':
        break

    for i in word:
        list_.append(T.count(i))

    sum_ = sum(list_)
    print(sum_)