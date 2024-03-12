def solution(my_string, n):
    result = "" # 초기화 안 하면 오류
    for char in my_string: # my_string의 문자 반복
        result += char * n # 문자를 `n` 번 반복하여 이어붙인다
    return result

# 입력
try:
    input_string = input("문자열을 입력하세요: ")
    repeat_count = int(input("반복 횟수를 입력하세요: "))

    # 결과 출력
    result = solution(input_string, repeat_count)
    print("결과:", result)

except ValueError:
    print("올바른 입력값을 입력하세요.")
