def solution(numbers):
    answer = 0
    sum = 0 # 변수 설정

    for i in range(len(numbers)):
        sum += numbers[i] # 리스트 합계

    answer = sum / len(numbers)
    return answer # 평균 계산

# 숫자 리스트 입력
user_input = input("숫자를 입력하세요 (쉼표로 구분): ")
numbers = [int(x) for x in user_input.split(",")]

# 결과 출력
result = solution(numbers)
print(f"평균: {result}")
