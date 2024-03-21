def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

# 입력
number = int(input("숫자를 입력하세요: "))
n = int(input("배수를 입력하세요: "))
m = int(input("배수를 입력하세요: "))

# 결과 출력
result = solution(number, n, m)
print(result)
