def solution(a, b):

    # 정수를 문자열로 변환
    aa = str(a)
    bb = str(b)

    # 문자열을 합쳐서 정수로 변환
    aabb = int(aa + bb)
    aabb2 = 2 * a * b

    # 조건에 따라 결과 값 설정
    if aabb >= aabb2:
        return aabb
    else:
        return aabb2
    # 입력
a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))
    # 출력
result = solution(a, b)
print("결과:", result)
