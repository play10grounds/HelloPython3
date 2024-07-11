# 수식/표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자
# 자료형 승격promotion

# 매출액 입력시 총합 출력
sale1 = int(input('1월 매출 : '))
sale2 = int(input('2월 매출 : '))
sale3 = int(input('3월 매출 : '))
totalSale = sale1 + sale2 + sale3

print(f'1분기 전체 매출 : {totalSale} 원')

# 1분기 수익 계산
sales = int(input('1분기 매출 : '))
buys = int(input('1분기 매입 : '))
profit = sales - buys

print(f'수익 : {profit} 원')

# 방의 넓이 구하기
width = int(input('가로 길이 : '))
height = int(input('세로 길이 : '))
area = width * height

print(f'넓이 : {area} ㎠')

# 신체질량지수BMI 구하기
weight = float(input('몸무게(kg) : '))
height = float(input('신장(m) : '))
bmi = int((weight / (height * height)))

print(f'BMI : {bmi}')

# 홀짝 게임
coins = int(input('손안에 동전수를 입력하세요 : '))
result = coins % 2

print(f'{result}')
print(f'{coins % 2}')

# 빵 나누기
breads = 97
divsor = 3
studs = 97 // 3
mods = 97 % 3

print(f'''
빵을 나누어 줄 수 있는 학생수 : {studs}
남는 빵 갯수 : {mods}
''')


# 전염병 예상 감염자 구하기
# 1일차 -> 2명
# 2일차 -> 4명
# 3일차 -> 8명
# 4일차 -> 16명
# n일차 -> 2 ** n명
infectors = 2 ** 30

print(f'30일 이후 예상 감염자 수 : {infectors}')


# 할당 연산자

# 논리 연산자

# 논리 연산자 단축식 평가

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 참일때값 if 조건식 else 거짓일때값

myScore = 75
result = '합격!' if myScore >= 90 else '불합격!'

print(result)


# 복리 계산기
money = 5_000_000
rate = 0.05
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액

print(f'5년 후 총 수령액 : {int(money):,} 원')

# 범퍼카 탑승
child = int(input('어린이의 신장을 입력하세요 : '))
isRide = (child >= 120)

print(f'{isRide}')


# 범퍼카 탑승 가능 판별
child = int(input('어린이의 신장을 입력하세요 : '))
isRide = (child >= 120) & (child < 170)

print(f'{isRide}')


# 적자/흑자 판별
income = int(input('수입은? '))
outcome = int(input('지출은? '))

result = '흑자' if (income > outcome) else '적자'
print(f'{result}')

