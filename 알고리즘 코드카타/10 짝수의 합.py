def solution(n):
    answer = 0
    for i in range(1, n+1): # 1부터 n까지의 숫자를 반복
        if i % 2 == 0: # 짝수인지 판별
            answer += i # 숫자 더하기
    return answer

# 숫자 입력
try:
    n = int(input("숫자를 입력하세요: "))

    # 결과 출력
    result = solution(n)
    print(f"1부터 {n}까지의 짝수의 합은 {result}입니다.")

except ValueError: # 예외
    print("올바른 숫자를 입력하세요.")