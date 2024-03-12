def solution(my_string):
    answer = 0

    for char in my_string:
        if '0' < char <= '9': # 0보다는 크고 9보다는 같거나 작으면
            answer += int(char) # 문자를 정수로 변환

    return answer

#  문자열 입력 받기
input_string = input("문자열을 입력하세요: ")
result = solution(input_string)
# 출력
print(f"결과: {result}")
