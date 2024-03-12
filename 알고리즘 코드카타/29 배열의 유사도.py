def solution(s1, s2): # 문자열 2개 (s1, s2)
    answer = 0
    for word1 in s1: # s1와 s2 문자열 비교하여 공통된 문자 수를
        for word2 in s2:
            if word1 == word2:
                answer += 1 # 같은 문자 수를 카운트 하다
    return answer

# 입력
s1 = input("첫 번째 문자열을 입력하세요 (공백으로 구분): ").split()
s2 = input("두 번째 문자열을 입력하세요 (공백으로 구분): ").split()
# 결과 출력
result = solution(s1, s2)
print(f"공통된 단어의 수: {result}")