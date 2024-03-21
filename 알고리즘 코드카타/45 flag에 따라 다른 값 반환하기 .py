def solution(a, b, flag):
    if not flag: # 거짓인지 판별 (참,거짓 중 하나)
        return a - b # 거짓이면 a와 b를 뺀 결과
    else:
        return a + b # 참이면 a와 b를 더한 결과

# 입력
a = int(input("정수 a를 입력하세요: "))
b = int(input("정수 b를 입력하세요: "))
flag = bool(input("True 또는 False 중 하나를 입력하세요: "))

# 결과 출력
result = solution(a, b, flag)
print("결과:", result)
