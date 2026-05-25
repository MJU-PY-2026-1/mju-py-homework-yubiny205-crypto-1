print('자취 라이프 매니저 - 냉장고 관리 시스템')

name = input('사용자 이름:')
monthly_budget = int(input('이번달 식비 예산:'))

warning_rate = 50.0
total_price = 0

food_names = []
food_prices = []
food_dates = []
nutrition_scores = []

def show_menu():
    print('\n===== 자취 라이프 매니저 메뉴 =====')
    print('1. 신규 식재료 등록')
    print('2. 냉장고 식재료 전체 출력')
    print('3. 식비 점유율 및 남은 예산 확인')
    print('4. 지출 등급 판정')
    print('5. 알뜰 자취왕 칭호 확인')
    print('6. 유통기한 임박 식재료 확인')
    print('0. 프로그램 종료')
    print('==================================')

def add_food():
    global total_price

    print('\n[신규 식재료 등록]')
    food_name = input('식재료 이름:')
    price = int(input('가격:'))
    date = int(input('남은 유통기한(일):'))
    nutrition = float(input('영양 점수(0~10): '))

    food_names.append(food_name)
    food_prices.append(price)
    food_dates.append(date)
    nutrition_scores.append(nutrition)

    total_price += price

    print(f'{food_name} 등록이 완료되었습니다.')

def show_food_list():
    print('\n[냉장고 식재료 전체 목록]')

    if len(food_names) == 0:
        print('아직 등록된 식재료가 없습니다.')
    else: 
        for i in range(len(food_names)):
            print(f'{i+1}, {food_names[i]} / 가격: {food_prices[i]}원 / 유통기한: {food_dates[i]}일 / 영양 점수: {nutrition_scores[i]}점')

def calculate_budget_rate(total, budget):
    if budget > 0:
        rate = (total / budget) * 100
    else:
        rate = 0

    return rate

def show_budget_status():
    remaining_budget = monthly_budget - total_price
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    print('\n[식비 점유율 및 남은 예산 확인]')
    print(f'총 지출 금액: {total_price}원')
    print(f'남은 예산:{remaining_budget}원')
    print(f'식비 점유율: {budget_rate: .2f}%%')

def judge_spending():
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    print('\n[지출 등급 판정]')

    if budget_rate >= warning_rate:
        print('지출 등급: 과소비 주의')
    elif budget_rate >= 30:
        print('지출 등급: 적정 소비')
    else: 
        print('지출 등급: 알뜰 소비')

def check_title():
    remaining_budget = monthly_budget - total_price
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    if len(nutrition_scores) > 0:
        average_nutrition = sum(nutrition_scores) / len(nutrition_scores)
    else:
        average_nutrition = 0

    print('\n[특별 칭호 확인]')

    if remaining_budget > 0:
        if budget_rate < 30 and average_nutrition >= 7:
            print('특별 칭호: 알뜰 자취왕')
        elif budget_rate < 50 or average_nutrition >= 6:
            print('특별 칭호: 절약 연습생')
        else: 
            print('특별 칭호: 자취 입문자')
    else: 
        print('예산을 초과했습니다.')
        if not remaining_budget > 0:
            print('다음 장보기에서는 가격을 조금 더 신경 써야 합니다.')

def check_expiring_food():
    print('\n[유통기한 임박 식재료 확인]')

    if len(food_names) == 0:
        print('아직 등록된 식재료가 없습니다.')
    else:
        found = False

        for i in range(len(food_names)):
            if food_dates[i] <= 3:
                print(f'{food_names[i]}: 유통기한이 {food_dates[i]}일 남았습니다.')
                found = True

        if not found:
            print('유통기한이 임박한 식재료가 없습니다.')

while True:
    show_menu()
    menu = input('메뉴 번호를 선택하세요: ')

    if menu == '1':
        add_food()
    elif menu == '2':
        show_food_list()
    elif menu == '3':
        show_budget_status()
    elif menu == '4':
        judge_spending()
    elif menu == '5':
        check_title()
    elif menu == '6':
        check_expiring_food()
    elif menu == '0':
        print('\n자취 라이프 매니저를 종료합니다.')
        print(f'{name}님의 냉장고 관리를 마칩니다.')
        break
    else: 
        print('잘못된 메뉴 번호입니다. 다시 선택해주세요.')
