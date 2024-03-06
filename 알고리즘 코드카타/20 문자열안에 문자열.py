def solution(str1, str2): # 문자열 `str2`, 문자열 `str1`
    if str2 in str1:
        answer = 1  # 문자열 `str2`가 문자열 `str1`에 포함되어 있다면 answer = 1
    else:
        answer = 2 # 문자열 `str2`가 문자열 `str1`에 포함되어 있지 않다면 answer = 2

    return answer

# 문자열 입력
input_str1 = input("첫 번째 문자열을 입력하세요: ")
input_str2 = input("두 번째 문자열을 입력하세요: ")

# 결과 출력
result = solution(input_str1, input_str2)
if result == 1:
    print("첫 번째 문자열이 두 번째 문자열에 포함됩니다.")
else:
    print("첫 번째 문자열이 두 번째 문자열에 포함되지 않습니다.")
