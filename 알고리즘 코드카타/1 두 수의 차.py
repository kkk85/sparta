def numbers():
    # 숫자 입력
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if -50000 <= num1 <= 50000 and -50000 <= num2 <= 50000: # 제한사항
            result = num1 - num2 # 두 수의 차
            print(f"{num1}와 {num2}의 차는 {result}입니다.") # 결과 출력
        else:
            print("입력 범위를 초과하였습니다. -50000에서 50000까지의 숫자를 입력하세요.") # 입력 범위 초과

    except ValueError: # 예외
        print("올바른 숫자를 입력하세요.")

# 함수 호출
numbers()
