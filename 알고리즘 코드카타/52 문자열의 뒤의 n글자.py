def solution(my_string, n):
    # 문자열의 뒤에서부터 n개의 문자 반환
    return my_string[-n:]

# 사용자로부터 문자열과 n을 입력받기
user_string = input("문자열을 입력하세요: ")
user_n = int(input("뒤의 몇 번째 입력하세요: "))

# 출력
result = solution(user_string, user_n)
print("결과:", result)
