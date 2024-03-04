def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer

# 숫자 입력
try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 결과 출력
    result = solution(num1, num2)
    print(f"값: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")