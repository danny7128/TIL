# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# 특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.
# 해당 유니코드 숫자를 문자로 반환하는 함수는 chr이다. 

word = input()
for words in word:
    if ord(words)>= 97 and ord(words)<=122:
        print(chr(ord(words)-32),end = '')
    elif 65<= ord(words) and ord(words)<=90:
        print(chr(ord(words)+32),end = '')