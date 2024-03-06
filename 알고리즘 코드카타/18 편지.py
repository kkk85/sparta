def solution(message):
    char_list = list(message)
    answer = len(char_list) * 2
    return char_list

# 입력
input_message = input("문자열을 입력하세요: ")
result = solution(input_message)
print(f"결과: {result}")
