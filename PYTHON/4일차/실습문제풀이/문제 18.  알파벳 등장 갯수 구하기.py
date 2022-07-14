# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'
dic = {}
for words in word:
    if words in dic:
        dic[words] +=1
    else:
        dic[words] = 1

for key in list(dic.keys()):
    print(key ,dic[key])