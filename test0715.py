아이스 아메리카노

def solution(money):
    Ice = 5500
    count = 0
    count = money % Ice
    
    count2 = 0
    count2 = money // Ice
    
    answer = []
    answer.append(count2)
    answer.append(count)
    return answer