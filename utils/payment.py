## MovieReservationProject/cinemapps/payment.py
import time
# 시간딜레이를 임의로 주기위한 패키지 import.

def pay_card():
    # 함수 정의, 매개변수x
    print('카드를 꽂아주세요.')
    print('결제중..\n')
    time.sleep(2)
    # 결제가 넘어가는데 2초 임의로 딜레이를 준다.
    print('결제가 완료되었습니다.')

def pay_cash(ttl_amnt):
    # 함수정의, 매개변수: 결제할 총 금액
    pymn = int(input('투입 하실 금액을 입력하세요: '))
    # 투입금액을 입력받아 정수로 형변환한다,
    if pymn < ttl_amnt:
        # 투입금액이 결제 금액보다 모자르면
        print(f'금액이 {ttl_amnt - pymn}원 모자릅니다.')
        # 모자를 금액 출력
        exit()
        # 프로그램 종료
    elif pymn == ttl_amnt:
        # 투입금액과 결제 금액이 같다면
        print('결제가 완료되었습니다.')
        # 결제완료
    else:
        # 투입금액이 결제금액보다 크다면 거스름돈 출력
        change = pymn - ttl_amnt
        # 잔돈 = 투입금액 - 결제금액
        krw50000 = int(change / 50000)
        # 50000으로 나눈 몫 만큼 지급
        change = change % 50000
        # 50000으로 나눈 나머지를 다시 할당
        krw10000 = int(change / 10000)
        # 10000으로 나눈 몫 만큼 장수지급
        change = change % 10000
        # 10000으로 나눈 나머지를 다시 할당.
        krw5000 = int(change / 5000)
        # 5000으로 나눈 몫 만큼 장수지급
        change = change % 5000
        # 5000으로 나눈 나머지를 다시 할당.
        krw1000 = int(change / 1000)
        # 1000으로 나눈 몫 만큼 장수지급
        change = change % 1000
        # 1000으로 나눈 나머지를 다시 할당.

        print('--거스름돈--'.center(20))
        # 20칸 가운데 정렬 출력
        print(f"50000원권 : {krw50000}장")
        # 해당범주에 맞는 지폐 장수 출력
        print(f"10000원권 : {krw10000}장")
        # 해당범주에 맞는 지폐 장수 출력
        print(f"5000원권 : {krw5000}장")
        # 해당범주에 맞는 지폐 장수 출력
        print(f"1000원권 : {krw1000}장")
        # 해당범주에 맞는 지폐 장수 출력
        print(f"동전:         {change}원")
        # 남은 동전 출력
        print('결제가 완료되었습니다.')