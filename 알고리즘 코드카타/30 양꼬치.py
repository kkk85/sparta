def solution(n, k): # 양꼬치: n 음료수: k
    answer = 0
    num = n

    if n >= 10:
        k -= n // 10 # n이 10으로 나누어진 몫을 k에서 뺀다

    answer = n * 12000 + k * 2000 #n × 12000 + k × 2000 = answer
    return answer

# 입력
n = int(input("양꼬치 몇 인분: "))
k = int(input("음료수 몇 개: "))

# 결과 출력
result = solution(n, k)
print(f"총 계산: {result}")
