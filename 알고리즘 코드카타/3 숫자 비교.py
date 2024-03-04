def solution(num1, num2):
    if 0 <= num1 <= 10000 and 0 <= num2 <= 10000:  # 제한사항
        if num1 == num2: # 두 수가 같으면 1 다르면 -1로 리턴
            return 1
        else:
            return -1
    else:
        return 0  # 제한사항을 벗어날 경우 반환
# 숫자 입력
try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 결과 출력
    result = solution(num1, num2)
    if result == 0:
        print("입력 범위를 초과하였습니다. 0에서 10000까지의 숫자를 입력하세요.")
    else:
        print(f"결과: {result}")

except ValueError: # 예외
    print("올바른 숫자를 입력하세요.")
