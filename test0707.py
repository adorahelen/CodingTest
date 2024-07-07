어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = n ** 0.5
    if n == int(answer) * int(answer) :
        answer = 1
    elif n != n*n : 
        answer = 2 
    return answer


int () 안해줘서 80점으로 두번 틀림, 컴퓨터 너무 싫어용


정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요

def solution(numbers):
    i = 0
    while i < len(numbers):
        numbers[i] = numbers[i] * 2 
        i += 1
    answer = numbers
    return answer