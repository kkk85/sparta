def solution(my_string):
    answer = my_string.lower() # 문자열 소문자로 변환하고 저장하는
    return answer

# 입력
input_string = input("문자열을 입력하세요: ")
result = solution(input_string)
print("결과:", result)