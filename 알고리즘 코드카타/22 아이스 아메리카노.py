def solution(money: int) -> list: # 함수가 리스트로 반환될 것이라는 Python의 타입 힌트
    return [money // 5500, money % 5500] # money를 5500로 나눈 몫과 나머지를 구한다

# 입력
user_money = int(input("금액을 입력하세요: "))

# 결과 출력
result = solution(user_money)
print(f"아이스 아메리카노 몇 잔: {result[0]}, 잔돈: {result[1]}")
