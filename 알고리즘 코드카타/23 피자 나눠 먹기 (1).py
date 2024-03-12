def solution(n):
    # 피자 한 판이 7조각 그리고 사람 수에 따라 따라 몇 판이 필요한지 계산 (삼항 연산자)
    num_pans = n // 7 if n % 7 == 0 else n // 7 + 1
    # n % 7 == 0: 입력값이 7의 배수, n % 7 != 0: 입력값이 7의 배수가 아니 경우,
    # else n // 7 + 1: 추가로 판이 필요하지 않으면 1을 더해 나머지 조각을 포함하여 출력한다
    return num_pans

# 입력
try:
    n = int(input("사람 수를 입력하세요: "))
    result = solution(n)
    print(f"{n}명이 최소 한 조각씩 먹기 위해서 {result}판이 필요합니다.")
except ValueError: # 예외
    print("올바른 숫자를 입력하세요.")
