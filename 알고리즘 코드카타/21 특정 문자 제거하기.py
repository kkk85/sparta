def solution(my_string, letter):
    modified_string = my_string.replace(letter, '') # 함수 `str.replace()`: 일부 단어라도 일치하면 다른 문자열로 바꾼다.
    # 즉,(letter, '') 제거할 문자를 빼고 출력한다

    return modified_string

# 입력
user_string = input("문자열을 입력하세요: ")
user_letter = input("제거할 문자를 입력하세요: ")

# 결과 출력
result = solution(user_string, user_letter)
print(f"결과: {result}")
