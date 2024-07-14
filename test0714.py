n = int(input(" :  "))


def solution(n):
    listlist = []
    i = 0
    while i < n:
        i +=1
        if i % 2 == 1 : 
            listlist.append(i)
    
    answer = listlist    
    return answer


result = solution(n)

print(result)