print('자취 라이프 매니저 - 냉장고 관리 시스템')

name = input('사용자 이름:')
monthly_budget = int(input('이번달 식비 예산:'))
warning_rate = 50.0
total_price = 0

food_names = []
food_prices = []
food_dates = []
nutrition_scores = []

print('\n식재료 3개를 등록합니다.')

for i in range(3):
    print(f'\n{i+1}번째 식재료 입력')
    food_name = input('식재료 이름:')
    price = int(input('가격:'))
    date = int(input('남은 유통기한(일):'))
    nutrition = float(input('영양 점수(0~10): '))

    food_names.append(food_name)
    food_prices.append(price)
    food_dates.append(date)
    nutrition_scores.append(nutrition)

    total_price += price

food_names.insert(0, '냉장고 목록')
food_prices.sort()

food_count = len(food_dates)
max_price = max(food_prices)
total_nutrition = sum(nutrition_scores)
average_nutrition = total_nutrition / 3

remaining_budget = monthly_budget - total_price
budget_rate = (total_price / monthly_budget) * 100

print(f'등록한 식재료 개수: {food_count}개')
print(f'총 지출 금액: {total_price}원')
print(f'남은 예산:{remaining_budget}원')
print(f'식비 점유율: {budget_rate: .2f}%%')

if budget_rate >= warning_rate:
    print('지출 등급: 과소비 주의')
elif budget_rate >= 30:
    print('지출 등급: 적정 소비')
else: 
    print('지출 등급: 알뜰 소비')

if remaining_budget > 0:
    if budget_rate < 30 and average_nutrition >= 7:
        print('특별 칭호: 알뜰 자취왕')
    elif budget_rate < 50 or average_nutrition >= 6:
        print('특별 칭호: 절약 연습생')
else: 
    print('예산을 초과했습니다.')
    if not remaining_budget > 0:
        print('다음 장보기에서는 가격을 조금 더 신경 써야 합니다.')

print('\n[냉장고 식재료 이름 목록]')
print(food_names)

print('\n[가격 오름차순 목록]')
print(food_prices)

print('\n프로그램을 종료합니다.')