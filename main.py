print('자취 라이프 매니저 - 냉장고 관리 시스템 V3.0')

name = input('사용자 이름: ')

while True:
    try:
        monthly_budget = int(input('이번달 식비 예산: '))
        break
    except ValueError:
        print('예산은 숫자로 입력해주세요.')

warning_rate = 50.0
file_name = 'fridge_data.txt'

foods = []

def show_menu():
    print('\n===== 자취 라이프 매니저 메뉴 =====')
    print('1. 신규 식재료 등록')
    print('2. 냉장고 식재료 전체 출력')
    print('3. 식비 점유율 및 남은 예산 확인')
    print('4. 지출 등급 판정')
    print('5. 알뜰 자취왕 칭호 확인')
    print('6. 유통기한 임박 식재료 확인')
    print('7. 냉장고 데이터 파일 저장')
    print('8. 냉장고 데이터 파일 불러오기')
    print('0. 프로그램 종료')
    print('==================================')


def input_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print('숫자로 입력해주세요.')


def input_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print('숫자로 입력해주세요.')


def get_total_price():
    total = 0

    for food in foods:
        total += food[1]

    return total


def add_food():
    print('\n[신규 식재료 등록]')

    food_name = input('식재료 이름: ')
    price = input_int('가격: ')
    date = input_int('남은 유통기한(일): ')
    nutrition = input_float('영양 점수(0~10): ')

    food = [food_name, price, date, nutrition]
    foods.append(food)

    print(f'{food_name} 등록이 완료되었습니다.')


def show_food_list():
    print('\n[냉장고 식재료 전체 목록]')

    if len(foods) == 0:
        print('아직 등록된 식재료가 없습니다.')
    else:
        headers = ['식재료 이름', '가격', '남은 유통기한', '영양 점수']

        for i in range(len(foods)):
            print(f'\n[{i + 1}번 식재료]')

            # 이중 순회 출력
            for j in range(len(foods[i])):
                if j == 1:
                    print(f'{headers[j]}: {foods[i][j]}원')
                elif j == 2:
                    print(f'{headers[j]}: {foods[i][j]}일')
                elif j == 3:
                    print(f'{headers[j]}: {foods[i][j]}점')
                else:
                    print(f'{headers[j]}: {foods[i][j]}')


def calculate_budget_rate(total, budget):
    if budget > 0:
        rate = (total / budget) * 100
    else:
        rate = 0

    return rate


def show_budget_status():
    total_price = get_total_price()
    remaining_budget = monthly_budget - total_price
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    print('\n[식비 점유율 및 남은 예산 확인]')
    print(f'총 지출 금액: {total_price}원')
    print(f'남은 예산: {remaining_budget}원')
    print(f'식비 점유율: {budget_rate:.2f}%')


def judge_spending():
    total_price = get_total_price()
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    print('\n[지출 등급 판정]')

    if budget_rate >= warning_rate:
        print('지출 등급: 과소비 주의')
    elif budget_rate >= 30:
        print('지출 등급: 적정 소비')
    else:
        print('지출 등급: 알뜰 소비')


def check_title():
    total_price = get_total_price()
    remaining_budget = monthly_budget - total_price
    budget_rate = calculate_budget_rate(total_price, monthly_budget)

    nutrition_total = 0

    for food in foods:
        nutrition_total += food[3]

    if len(foods) > 0:
        average_nutrition = nutrition_total / len(foods)
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
        print('다음 장보기에서는 가격을 조금 더 신경 써야 합니다.')


def check_expiring_food():
    print('\n[유통기한 임박 식재료 확인]')

    if len(foods) == 0:
        print('아직 등록된 식재료가 없습니다.')
    else:
        found = False

        for food in foods:
            if food[2] <= 3:
                print(f'{food[0]}: 유통기한이 {food[2]}일 남았습니다.')
                found = True

        if not found:
            print('유통기한이 임박한 식재료가 없습니다.')


def save_food_data():
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for food in foods:
                file.write(f'{food[0]},{food[1]},{food[2]},{food[3]}\n')

        print(f'{file_name} 파일 저장이 완료되었습니다.')

    except:
        print('파일 저장 중 오류가 발생했습니다.')


def load_food_data():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            foods.clear()

            for line in file:
                data = line.strip().split(',')

                food_name = data[0]
                price = int(data[1])
                date = int(data[2])
                nutrition = float(data[3])

                foods.append([food_name, price, date, nutrition])

        print(f'{file_name} 파일 불러오기가 완료되었습니다.')

    except FileNotFoundError:
        print('저장된 파일이 없습니다. 먼저 식재료를 등록하고 저장해주세요.')

    except ValueError:
        print('파일 안의 숫자 데이터 형식이 잘못되었습니다.')

    except:
        print('파일 불러오기 중 오류가 발생했습니다.')


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
    elif menu == '7':
        save_food_data()
    elif menu == '8':
        load_food_data()
    elif menu == '0':
        save_food_data()
        print('\n자취 라이프 매니저를 종료합니다.')
        print(f'{name}님의 냉장고 관리를 마칩니다.')
        break
    else:
        print('잘못된 메뉴 번호입니다. 다시 선택해주세요.')