def calculate_birth_year(age):
    current_year = 2022
    birth_year = current_year - age
    return birth_year

# 사용자로부터 나이 입력 받기
try:
    age = int(input("나이를 입력하세요: "))
    birth_year = calculate_birth_year(age)
    print(f"2022년 기준 {age}살이므로 {birth_year}년생입니다.")
except ValueError:
    print("올바른 나이를 입력하세요.")