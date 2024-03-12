def solution(price):
    if price >= 500000:
        price *= 0.8 # price가 500,000 이상 20% 할인
    elif price >= 300000:
        price *= 0.9 # # price가 300,000 이상 10% 할인
    elif price >= 100000:
        price *= 0.95 # price가 100,000 이상 5% 할인
    return int(price)

# 가격 입력
try:
    input_price = float(input("가격을 입력하세요: "))

    # 결과 출력
    result = solution(input_price)
    print("결과:", result)

except ValueError:
    print("올바른 입력값을 입력하세요.")
