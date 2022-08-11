import sys

sys.stdin = open('BOJ_2495.txt')



























# for _ in range(3):                  # 각 줄에 하나씩 세 개의 양의 정수가 주어짐
#   num = list(input())               # 숫자 입력받아 배열로 나누기
#   arr = [num[0]]                    # 첫번째 숫자 담기
#   answer = [1]                      # 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하기 위해 1을 저장해둠
#   cnt = 1                           # arr에 숫자가 하나 담겼기 때문에 cnt에 1 저장
#   for i in range(1, 8):             # 숫자는 여덟 자리의 양의 정수기 때문에 7번 반복
#     if(arr[len(arr)-1]==num[i]):    # arr에 담겨있는 숫자와 현재 숫자가 같다면
#       cnt += 1                      # 일을 추가함
#     else:                           # 아니라면
#       arr.append(num[i])            # 그 수를 arr에 추가하고
#       answer.append(cnt)            # cnt값을 answer에 저장
#       cnt = 1                       # cnt는 1로 초기화
#                                     # 계속해서 arr에 담겨있는 숫자와 현재 숫자가 같아 저장이 되지 않았을 cnt를 위해서 answer에 cnt추가
#   answer.append(cnt)
#   print(max(answer))                # 그 중 가장 큰 값을 출력하기 위해서 max 활용
