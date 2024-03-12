def solution(my_string):
    answer = my_string
    vowels = ["a", "e", "i", "o", "u"] # 제거할 문자열 리스트

    for v in vowels: #  리스트 vowels 각 모음 반복
        answer = answer.replace(v, "") # v를 빈 문자열로 대체합니다. 해당 모음 제거

    return answer

# 문자열 입력
try:
    input_string = input("문자열을 입력하세요: ")

    # 결과 출력
    result = solution(input_string)
    print("결과:", result)

except ValueError:
    print("올바른 문자열을 입력하세요.")
