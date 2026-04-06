# 파일이름 : 자취 라이 매니저
# 작 성 자 : 주유빈
# [1차 과제] 자취 라이프 매니저: 일일 식비 관리 및 유통기한 기록
# 목표: 일일 예산 대비 지출 계산 및 식재료 보관 정보 출력

print("="*45)
print("   자취 라이프 매니저 V1.0 (오늘의 식비)   ")
print("="*45)

# 1. 사용자 및 예산 정보 입력 (문자열, 정수)
user_name = input("자취생 이름을 입력하세요: ")
daily_budget = int(input("오늘 사용할 수 있는 식비 예산은 얼마인가요?(원): "))

# 2. 식재료 정보 및 유통기한 입력 (문자열, 정수, 실수)
item_name = input("오늘 구매한 식재료 이름: ")
item_unit_price = int(input(f"'{item_name}'의 1개당 가격은 얼마인가요?(원): "))
item_count = float(input(f"'{item_name}'을 몇 개 구매하셨나요?(예: 0.5, 2): "))
expiry_date = input(f"'{item_name}'의 유통기한은 언제까지인가요?(예: 2024-12-31): ")

# 3. 데이터 계산 (산술 연산)
# 오늘 총 지출액 계산 (단가 * 개수)
total_expense = int(item_unit_price * item_count)

# 남은 예산(저축액) 계산
remaining_savings = daily_budget - total_expense

# 4. 결과 출력 (f-string 활용)
print("\n" + "*"*45)
print(f" [{user_name}님의 오늘의 알뜰 리포트] ")
print("*"*45)
print(f"▶ 오늘 사용한 총 지출: {total_expense:,}원")
print(f"▶ 지출 후 남은 예산: {remaining_savings:,}원")
print("-" * 45)
print(f"✨ 축하합니다! {remaining_savings:,}원을 저축하셨어요!")
print(f"📍 오늘의 식재료 '{item_name}'은 {expiry_date}까지 보관 가능합니다!")
print("*"*45)

print(f"\n오늘도 알뜰하게 생존 완료! {user_name}님, 좋은 저녁 되세요!")
