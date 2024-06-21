#built in Data type 

a = 13
b = 14

print(a / b)
print(a // b)
print(-a)
print(abs(-a))
print(a**b)

print( a and b)
print ( a or b)
print(not a )
#부동 소수형 데이터 연산 에러 == 앱실론 

#----------
#컬렉션 데이터 타입 1. 리스트 2. 튜플 3. 딕셔너리 4. 셋  5. 문자열 
# 이 컬렉션들은 데이터의 수정 가능 여부에 따라, 변경 가능한 객체 || 변경할 수 없는 객체 
# 뮤터블 객체 == 변경 O : 리스트, 딕셔너리, 셋
# 이뮤터블 객체 == 변경 X : 튜플 + (정수, 부동소수점, 문자열, 튜플) 

my_list = [1,2,3,4,5]
my_list[4] = 6
print(my_list)
#리스트 생성, 내부에 원소 변경

a = 4 
b = a
b += 2
print(a,b)

# 리스트 인덱싱, 리스트 슬라이싱
my_list = [1,2,3,4,5]
my_list2 = [1,3,5] + [7,9]
my_list3 = list(my_list)



# 딕셔너리
# 튜플 
# 문자열
# 함수 
# 코딩테스트 함수 사용법 
