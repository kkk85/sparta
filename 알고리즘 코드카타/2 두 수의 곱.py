def numbers():
    try: # 숫자 입력
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        result = num1 * num2 # 두 수의 곱
        print(f"{num1}와 {num2}의 곱은 {result}입니다.") # 결과 출력

    except ValueError: # 예외
        print("올바른 숫자를 입력하세요.")


# 함수 호출
numbers()
