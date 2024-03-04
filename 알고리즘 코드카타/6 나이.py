from datetime import datetime

def calculate_birth_year(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return birth_year

# 나이 입력
age = int(input("나이를 입력하세요: "))

birth_year = calculate_birth_year(age)

print(f"{age}살인 경우, 태어난 연도는 {birth_year}년입니다.")
