def solution(num1, num2):
    answer = num1//num2
    return answer

try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 함수 호출 및 결과 출력
    result = solution(num1, num2)
    print(f"몫: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")