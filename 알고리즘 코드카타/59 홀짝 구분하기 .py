def solution(n):
    if n % 2 == 0:
        return f"{n} is even" # 짝인경우 is even 출력
    else:
        return f"{n} is odd" # 홀인경우 is odd 출력

# 입력 받기
n = int(input("숫자: "))

# 함수 호출 및 결과 출력
result = solution(n)
print(result)
