문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):
    i = 0
    a = []
    while i < len(my_string):
        
        if letter != my_string[i]:
            a.append(my_string[i])
            i += 1
           
        elif letter == my_string[i]:
            i += 1
            
    
    b = ''.join(a)
    answer = b
    return answer

이걸 이렇게 힘들게 푸는게 맞나 


def solution(my_string, letter):
    return my_string.replace(letter, '')