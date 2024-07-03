머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 
양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

def solution(n, k):
    a = 12000
    b = 2000
    c = n // 10
    sum = 0
    sum = (n*a) + (k*b) - (c*b)
    answer = sum
    return answer

머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.

def solution(message):
    answer = len(message)*2
    return answer

정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    count = 0
    count2 = 0
    for i in range(len(num_list)):
        j = num_list[i] % 2
        if j == 0 : 
            count += 1
        else:
            count2 += 1
    answer = [0,0]
    answer[0] = count
    answer[1] = count2

    return answer