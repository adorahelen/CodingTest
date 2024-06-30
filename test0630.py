# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# def solution(array, n):
    
#     i = 0
#     j = 0
#     answer = 0
#     k = len(array)
#     while i < k:
#         j = array[i]
#         if j == n : answer += 1
#         i += 1
    
#     return answer
# 맞추긴 했는데, 잘 짠게 맞을까? ㅋㅋ


# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

# def solution(array, height):
#     answer = 0
#     i = 0
#     j = len(array)
#     k = 0
    
#     while i < j:
#         k = array[i]
#         if k > height : answer += 1
#         i += 1
        
#     return answer