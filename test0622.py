#정수 배열을 정렬해서 반환하는 함수를 작성해라
#입력 [1, -5, 2, 4, 3], [2, 1, 1, 3, 2, 5, 4], [6, 1, 7]
#출력 : 낮은 수 부터 오름차순으로 정렬 

def solution (arr):
    arr.sort()
    return arr
    #sort 메서드는 리스트를 역순으로 반환한다. 

def solution2 (arr):
    sorted_list = (sort(arr))
    return sorted_list

#배열 제어하기
def solution(lst):
    unique_lst = list(set(lst)) #중복값 제거 *SET 함수
    unique_lst.sort(reverse=True) #내림차순 정렬 
    return unique_lst

    #파이썬에는 코딩 테스트에 유용한 함수가 많다. => 직접 작성하지 말고 가져다 사용하라


#두개 뽑아서 더하기 
def solution(numbers):
    ret = [] #1. 빈 배열 생성
    #2. 두 수를 선택하는 모든 경우의 수를 반복문으로 구성 
    for i in range (len(numbers)):
        for j in range(i + 1, len(numbers)):
            #3. 두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers[j])
        #4. 중복된 값을 제거하고, 오름차순으로 정렬
    ret = sorted(set(ret))
    return ret #최종결과 반환