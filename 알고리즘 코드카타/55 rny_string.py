import re # re 모듈, 정규 표현식

def solution(rny_string):
    return re.sub(r'm', 'rn', rny_string) # 위에 있는 모듈 re.sub 함수를 이용 'm'을 "rn"으로 바꾼다

# 입력
input_string = input("문자열을 입력하세요: ")

# 결과
result = solution(input_string)
print("결과:", result)