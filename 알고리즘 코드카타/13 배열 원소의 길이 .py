def solution(strlist):
    return [len(s) for s in strlist] # 리스트 안에 있는 문자 함수로 반환

# 문자열 리스트 입력
strings = input("문자열 리스트를 입력하세요 (문자열 사이에 공백을 두고): ").split()

# 결과 출력
result = solution(strings)
print("각 문자열의 길이:", result)
