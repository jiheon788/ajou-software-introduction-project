## MovieReservationProject/main.py
import utils
# 프로그램을 실행하는데 필요한 기능들을 정의해놓은 'cinemapps' 패키지를 불러온다, main.py 에서는 ca로 호출한다.
import datetime
# 현재시간을 찍기 위한 패키지 import
import time
# 시간딜레이를 임의로 주기위한 패키지 import.
import pandas as pd
# 데이터베이스를 관리 하기위한 외부 패키지 import, main.py 에서는 pd로 호출한다.

reservationDB = []
# 예매내역 리스트를 빈 1차원 리스트로 생성한다. 프로그램 실행시 2차원리스트로 정보를 담을것이다. 이는 아래와 같다.
# reservationDB[[예약번호, 제목, 예약시간, 성인, 청소년, 유아, 총인원, 요금, 상영관, 상영시간, 인증코드, 자리번호...]]
reservation = 0
# Primary Key, 예약번호: 0으로 초기화 해둔다.

# 메인 프로그램
while True:
    # 무한loop 반복문
    utils.print_system_message("안녕하세요!")
    # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
    utils.print_system_menu()
    # ca패키지에서 함수 print_system_menu()을 실행한다. 매개변수와 반환값은 없다.
    sys_num = int(input("원하는 메뉴를 선택하세요: "))
    # 숫자를 입력받은 후 정수로 형변환하여 sys_num 변수에 할당한다.

    ### 시스템메뉴 > 프로그램 종료
    if sys_num == 3:
        # 3번 입력시 프로그램을 종료한다.
        utils.print_system_message("종료합니다.")
        # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
        exit()
        # 프로그램 종료

    ### 시스템메뉴 > 영화 예매
    elif sys_num == 1:
        # 1번 입력시 예매를 시작한다.
        reservationDB.append([])
        # 위에 만들어둔 1차원리스트에 차원을 부과하여 2차원 리스트로 만들어준다.
        utils.print_system_message("영화 예매를 시작합니다.")
        # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.

        #### 시스템메뉴 > 영화 예매 > 고객번호 :: reservationDB[reservation][0]
        reservationDB[reservation].append(reservation)
        # reservationDB[reservation]에 예약번호를 할당

        #### 시스템메뉴 > 영화 예매 > 영화선택 :: reservationDB[reservation][1]
        utils.print_movie_list()
        # ca패키지에서 함수 print_movie_list()를 실행한다. 매개변수와 반환값은 없다.
        film = int(input("영화 번호를 입력하세요:  "))
        # 숫자를 입력받은 후 정수로 형변환하여 film변수에 할당한다.
        if film == 1:
            # 1번 입력시
            reservationDB[reservation].append('Titanic')
            # reservationDB[reservation]에 선택한 영화제목을 apped
        elif film == 2:
            # 2번 입력시
            reservationDB[reservation].append('Avatar')
            # reservationDB[reservation]에 선택한 영화제목을 apped
        elif film == 3:
            # 3번 입력시
            reservationDB[reservation].append('Dune')
            # reservationDB[reservation]에 선택한 영화제목을 apped
        else:
            # 그 외 번호 입력시
            utils.print_system_message("잘못된 입력입니다.")
            # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
            exit()
            # 프로그램 종료

        #### 시스템메뉴 > 영화 예매 > 예매시각(현재시간) :: reservationDB[reservation][2]
        now = datetime.datetime.now()
        # datetime패키지의 now() 함수를 사용하여 현재시간을 now에 할당한다.
        reservationDB[reservation].append(now.strftime('%Y-%m-%d %H:%M:%S'))
        # reservationDB[reservation]에 현재시간을 주어진 포맷의 문자열로 할당한다. '년-월-일 시:분:초'

        #### 시스템메뉴 > 영화 예매 > 성인,청소년,유아 인원 수 입력
        adult, youth, infant = input('성인, 청소년, 유아 티켓 수를 입력하세요(n n n): ').split()
        # 숫자 세개를 간격을 두어 입력 받은 후 split하여 각각 세가지 변수에 할당한다.
        adult = int(adult)
        # 변수를 정수로 변환한 뒤 다시 저장
        youth = int(youth)
        # 변수를 정수로 변환한 뒤 다시 저장
        infant = int(infant)
        # 변수를 정수로 변환한 뒤 다시 저장
        reservationDB[reservation].append(adult)
        #### 성인 :: reservationDB[reservation][3]
        # reservationDB[reservation]에 성인 수를 append한다.
        reservationDB[reservation].append(youth)
        #### 청소년 :: reservationDB[reservation][4]
        # reservationDB[reservation]에 청소년 수를 append한다.
        reservationDB[reservation].append(infant)
        #### 유아 :: reservationDB[reservation][5]
        # reservationDB[reservation]에 유아 수를 append한다.

        #### 시스템메뉴 > 영화 예매 > 총 인원수:: reservationDB[reservation][6]
        total_people = adult + youth + infant
        # 성인 + 청소년 + 유아 수를 더해 총 인원을 구한다
        reservationDB[reservation].append(total_people)
        # reservationDB[reservation]에 총인원 수를 append한다.

        #### 시스템메뉴 > 영화 예매 > 요금 :: reservationDB[reservation][7]
        total_amount = 10000 * adult + 8000 * youth + 0 * infant
        # 성인 10000원, 청소년 8000원, 유아 0원으로 계산하여 총 요금을 할당한다.
        reservationDB[reservation].append(total_amount)
        # reservationDB[reservation]에 총 요금을 append한다.

        #### 시스템메뉴 > 영화 예매 > 상영관 & 상영시간
        selected_theater = utils.print_today_theater_n_choice(film)
        # utils 패키지의 print_today_theater_n_choice(film)함수에 매개변수로 영화번호를 입력하여, 상영관을 선택한 후 리스트로 값을 반환받는다.
        # selected_theater = [상영관키넘버, 상영관문자열, 상영시간문자열]
        reservationDB[reservation].append(selected_theater[1])
        #### 상영관 :: reservationDB[reservation][8]
        # reservationDB[reservation]에 상영관을 append한다.
        reservationDB[reservation].append(selected_theater[2])
        #### 상영시간 :: reservationDB[reservation][9]
        # reservationDB[reservation]에 상영시간을 append한다.

        #### 시스템메뉴 > 영화 예매 > 인증코드 :: reservationDB[reservation][10]
        authenticationCode = utils.generate_code()
        # ca패키지의 generate_code를 사용하여 인증코드를 받는다.
        reservationDB[reservation].append(authenticationCode)
        # reservationDB[reservation]에 상영시간을 append한다.

        #### 시스템메뉴 > 영화 예매 > 좌석예약 :: reservationDB[reservation][11~]
        for i in range(0, total_people):
            # 0부터 인원수-1까지 반복하여 인원 수 만큼 티켓을 예매한다.
            if selected_theater[0] == 1:
                # 위에서 입력받은 상영관키넘버 1번일 떄,
                x, y = utils.choice_seats(i, utils.Titanic_H1)
                # ca패키지의 Titanic_H1 상영관 과 i를 매개변수로 choice_seats(i, 상영관) 함수에 입력하여 x, y값을 반환 받는다.
            elif selected_theater[0] == 2:
                # 위에서 입력받은 상영관키넘버 2번일 떄,
                 x, y = utils.choice_seats(i, utils.Titanic_H2)
                 # ca패키지의 Titanic_H2 상영관 과 i를 매개변수로 choice_seats(i, 상영관) 함수에 입력하여 x, y값을 반환 받는다.
            elif selected_theater[0] == 3:
                # 위에서 입력받은 상영관키넘버 3번일 떄,
                 x, y = utils.choice_seats(i, utils.Avatar_H3)
                 # ca패키지의 Avatar_H3 상영관 과 i를 매개변수로 choice_seats(i, 상영관) 함수에 입력하여 x, y값을 반환 받는다.
            elif selected_theater[0] == 4:
                # 위에서 입력받은 상영관키넘버 4번일 떄,
                 x, y = utils.choice_seats(i, utils.Avatar_H4)
                 # ca패키지의 Avatar_H4상영관 과 i를 매개변수로 choice_seats(i, 상영관) 함수에 입력하여 x, y값을 반환 받는다.
            elif selected_theater[0] == 5:
                # 위에서 입력받은 상영관키넘버 5번일 떄,
                 x, y = utils.choice_seats(i, utils.Dune_H5)
                 # ca패키지의 Dune_H5 상영관 과 i를 매개변수로 choice_seats(i, 상영관) 함수에 입력하여 x, y값을 반환 받는다.
            reservationDB[reservation].append(f'{x}, {y}')
            # reservationDB[reservation]에 좌석좌표 x, y를 append한다.

        #### 시스템메뉴 > 영화 예매 > 예매내역출력 & 결제
        utils.print_system_message("결제창으로 넘어갑니다.")
        # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
        time.sleep(0.5)
        # 결제창으로 넘어가는데 0.5초 임의로 딜레이를 준다.
        print(f"=====예매내역 확인======")
        print(f"  영화          {reservationDB[reservation][1]}")
        # reservationDB[reservation][1] 내용을 출력한다.
        print(f"  상영관       {reservationDB[reservation][8]}")
        # reservationDB[reservation][8] 내용을 출력한다.
        print(f"  상영시간    {now.strftime('%Y년 %m월 %d일')} {reservationDB[reservation][9]}")
        # 위에서 datetime 패키지를 통해 받은 오늘의 날짜를 지정형식의 문자열로 가져와 reservationDB[reservation][9] 내용과 함께 출력한다.
        seat_num = 11
        # 좌석정보는 11열부터 나온다.
        for i in range(0, reservationDB[reservation][6]):
            # 0부터 인원수 - 1 까지 반복한다.
            print(f"  좌석          {reservationDB[reservation][seat_num]}")
            # 좌석정보 reservationDB[reservation][11] 부터 인원수 만큼 순차적으로 출력한다
            seat_num += 1
            # seat_num을 한자리 올려서 반복, 다음 좌석의 열번호이다.
        print(f"====================")
        print(f"  성인         {reservationDB[reservation][3]}명")
        # reservationDB[reservation][3] 내용을 출력한다.
        print(f"  청소년      {reservationDB[reservation][4]}명")
        # reservationDB[reservation][4] 내용을 출력한다.
        print(f"  유아         {reservationDB[reservation][5]}명")
        # reservationDB[reservation][5] 내용을 출력한다.
        print(f"====================")
        print(f"  Total         \\ {reservationDB[reservation][7]}\n")
        # 총 요금 출력한다, 원화 표시를 위해 \를 그대로 출력하려면 \\두번쓴다.
        pymn_methods = int(input("1. 카드    2. 현금: "))
        # 결제방식을 입력받아 정수로 변환 후 할당한다.

        #### 시스템메뉴 > 영화 예매 > 결제 > 카드
        if pymn_methods == 1:
            # 카드결제시,
            utils.pay_card()
            # ca패키지의 pay_card()실행.

        #### 시스템메뉴 > 영화 예매 > 결제 > 현금
        elif pymn_methods == 2:
            # 현금 결제시,
            utils.pay_cash(total_amount)
            # ca패키지의 pay_cash()실행.

        utils.print_system_message(f"예약완료!\n예약번호: {reservation}\n인증코드: {authenticationCode}\n티켓 출력시 예약번호와 인증코드가 필요합니다.")
        # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
        # 예약번호와 인증코드도 같이 보여준다. 추후 티켓출력시 인증을 위해 필요하다
        reservation += 1
        # 예약번호를 한자리 올리고 예매끝. 다시 while문 처음으로 돌아간다.

    ### 시스템메뉴 > 티켓 출력
    elif sys_num == 2:
        #sys_num 2번 티켓출력 선택
        reservation_num = int(input('예약번호를 입력하세요: '))
        #예약을 하고 받은 예약번호를 입력한다.
        if utils.customer_login(reservationDB[reservation_num][10]) == True:
            # ca패키지의 customer_login()함수에 매개변수로 예약번호에 해당하는 인증코드를 넣어 함수내부에서 코드를 입력받아 일치하는지 확인한다.
            # 일치하다면 True를 반환받아 인증성공
            utils.print_system_message("인증성공!")
            # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
            utils.print_ticket(reservationDB, reservation_num)
            # ca패키지의 print_ticket()함수, 예약리스트가 담긴  reservationDB와 출력하려는 예약번호를 매개변수로 넘긴다.
        else:
            # False를 반환받았다면 코드를 세번 틀린것. 인증실패
            utils.print_system_message("인증실패!")
            # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
            exit()
            #프로그램종료

    ### 시스템메뉴 > 관리자 채널
    elif sys_num == 0:
        #sys_num 0번 관리자탭 선택
        utils.print_system_message("관리자채널 입니다.")
        # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
        if utils.admin_login() == True:
            #ca패키지의 admin_login()함수 호출, 반환값이 True이면, 로그인성공
            utils.print_system_message("로그인 성공!")
            # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
            utils.print_admin_channel()
            # ca패키지의 print_admin_channel()함수 메뉴를 보여준다.
            admin_num = int(input("번호를 입력하세요: "))
            # 원하는 메뉴를 선택한다. 숫자를 문자로 입력받아 정수로 형변환한다.
            if admin_num == 1:
                # 1번 선택
                ReservationDatabase = pd.DataFrame(reservationDB)
                # 만들어진 이중리스트를 판다스 데이터프레임으로 변환하여 ReservationDatabase에 저장한다.
                print(ReservationDatabase)
                # 데이터 프레임을 출력한다.
            elif admin_num == 2:
                # 2번 선택
                timestamp = now.strftime('%Y%m%d')
                # 변수 now에 할당되어있는 현재시간을 주어진 포맷의 문자열로 할당한다. '년월일'
                ReservationDatabase = pd.DataFrame(reservationDB)
                # 만들어진 이중리스트를 판다스 데이터프레임으로 변환하여 ReservationDatabase에 저장한다.
                ReservationDatabase.to_csv(f'data/reservationDB{timestamp}.csv',index=False,header=False)
                # 데이터프레임 ReservationDatabase를 지정된 위치에 csv파일로만든다. 뒤에 년월일을 붙임, 인덱스 없고, 열이름도 지정하지 않는다.
                utils.print_system_message("DB저장완료")
                # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
        else:
            # 로그인 실패시 접속불가
            utils.print_system_message("로그인 실패!")
            # ca패키지의 print_system_message("message")를 실행한다. 매개변수로 출력할 메시지를 넣으면 함수에서 지정해둔 형식으로 출력해준다.
            break
            #프로그램종료
