def solution(num1, num2):
    if 0 <= num1 <= 100 and 0 <= num2 <= 100:  # 제한사항
        answer = num1 % num2
        return answer
    else:
        return None  # 제한사항을 벗어날 경우 None 반환

# 숫자 입력
try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 결과 출력
    result = solution(num1, num2)
    if result is not None:
        print(f"결과: {result}")
    else:
        print("입력 범위를 초과하였습니다. 0에서 100 사이의 숫자를 입력하세요.")

except ValueError:
    print("올바른 숫자를 입력하세요.")