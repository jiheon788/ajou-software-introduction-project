## MovieReservationProject/cinemapps/reservation.py
from pprint import pprint
# 리스트의 출력을 위한 pprint함수 impotr한다.
import time
# 임의의 딜레이를 위하여 time패키지 import한다.

## 함수 정의 > 시스템메뉴 출력
def print_system_menu():  # 매개변수x, 반환값x
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
    print("*                      MENU                        *")
    print("*                  ----------------                  *")
    print("*                                                       *")
    print("*  1.    영화 예매                                  *")
    print("*  2.    티켓 출력                                  *")
    print("*  3.    종료                                         *")
    print("*     ---------------------------------------     *")
    print("*  0.    관리자                                      *")
    print("*                                                       *")
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")

## 함수 정의 > 영화리스트 출력
def print_movie_list(): # 매개변수x, 반환값x
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
    print("*                   Movie List                      *")
    print("*                  ----------------                  *")
    print("*                                                       *")
    print("*   1. Titanic                                        *")
    print("*   2. Avatar                                        *")
    print("*   3. Dune                                          *")
    print("*                                                       *")
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")

## 함수 정의 > 상영관 정보
def print_today_theater_n_choice(flm):
    # 매개변수 선택한영화 번호, 반환값: [상영관키넘버, 상영관문자열, 상영시간문자열]
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
    print("*                Today`s Theaters                *")
    print("*                ----------------                    *")
    print("*                                                       *")
    print("*   상영영화     상영관         상영시간     *")
    print("*   ---------------------------------------       *")
    if flm == 1: # 매개변수 Titanic 영화 번호 들어오면 해당부분을 출력한다.
        print("*   1. Titanic      제 1상영관      10:30      *")
        print("*   2. Titanic      제 2상영관      21:40      *")
    elif flm == 2: # 매개변수 Avatar 영화 번호 들어오면 해당부분을 출력한다.
        print("*   3. Avatar       제 3상영관      15:45     *")
        print("*   4. Avatar       제 4상영관      18:50     *")
    elif flm == 3: # 매개변수 Dune 영화 번호 들어오면 해당부분을 출력한다.
        print("*   5. Dune      제 5상영관      20:00       *")
    print("*                                                       *")
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")

    theater_num = int(input('원하는 시간을 선택해주세요: '))
    # 번호를 입력받아 정수로 형변환한다.

    # 위 메뉴에서 시간대를 선택 후 번호를 입력받아, 정수로 형변환 후, 할당한다
    if theater_num == 1:
        # 1번 선택시
        return [theater_num, '제 1상영관', '10:30']
        # 해당하는 리스트를 반환한다.
    elif theater_num == 2:
        # 2번 선택시
        return [theater_num, '제 2상영관', '21:40']
        # 해당하는 리스트를 반환한다.
    elif theater_num == 3:
        # 3번 선택시
        return [theater_num, '제 3상영관', '15:45']
        # 해당하는 리스트를 반환한다.
    elif theater_num == 4:
        # 4번 선택시
        return [theater_num, '제 4상영관', '18:50']
        # 해당하는 리스트를 반환한다.
    elif theater_num == 5:
        # 5번 선택시
        return [theater_num, '제 5상영관', '20:00']
        # 해당하는 리스트를 반환한다.

## 함수 정의 > 좌석현황 출력
def print_seats(movie):
    # 선택한 상영관의 좌석정보가 담긴 이중리스트를 매개변수로 전달받아 출력해준다.
    print("=================")
    print("            SCREEN              ")
    print("=================")
    pprint(movie)
    #이중 for문을 사용하지 않아도 이중리스트를 출력해준다.
    print("===========| Gate |==")

## 함수 정의 > 자리 선택
def choice_seats(i, movie):
    #매개변수: i와 선택한 상영관의 좌석정보
    print_seats(movie)
    # 위 정의된 함수 출력, 좌석현황을 보여준다. 예약 1, 빈자리 0
    x, y = input(f'{i + 1}번쨰 자리를 입력하세요(10 10): ').split()
    # i는 0부터이기에 +1하여 순서를 알려준다.
    # 숫자 2개를 간격을 두어 입력 받은 후 split하여 각각 x, y 두가지 변수에 할당한다.
    x = int(x)  # 변수를 정수로 변환한 뒤 다시 저장
    y = int(y)  # 변수를 정수로 변환한 뒤 다시 저장
    if x > 10 or y > 10 :
        #범위 밖 번호를 입력시 안내문 출력 후 종료
        print('없는 좌석입니다.')
        exit()
    if movie[x - 1][y - 1] == 1:
        # 리스트의 인덱스도 0부터 시작한다. 고로 입력받은 번호 - 1 해준다
        # 선택한 자리가 이미 1이면, 해당좌석은 예약이 되어 있는 자리다.
        # 예약불가 안내메시지 출력 후, 종료.
        print('이미 예약된 좌석입니다.')
        exit()
    movie[x - 1][y - 1] = 1
    # 위 두가지 조건문에 걸리지 않으면 선택한 자리를 1로 바꾸어준다.
    return x, y # 선택된 좌석좌표를 반환한다.

# 함수 정의 > 티켓 및 예매내역 출력
def print_ticket(rsrvtDB, rsrvt):
    # 함수 정의, 매개변수로 예약내역이 모두 담긴 이중리스트, 예약변호를 받는다.
    print('출력중..\n')
    time.sleep(2)
    # 넘어가는데 2초 임의로 딜레이를 준다.
    print("|", "".center(33, 'V'), "|")
    # 33칸 가운데 정렬 나머지는 V로채운다.
    print("|", "Ticket".center(59, ' '), "|")
    # 59칸 가운데 정렬 나머진 공백으로 채운다.
    print("| ", "".center(58, ' '), " |")
    # 공백으로 58칸 가운데정렬
    time.sleep(0.5)
    # 결제가 넘어가는데 0.5초 임의로 딜레이를 준다.
    print("| ".ljust(6), f"{rsrvtDB[rsrvt][2]}".ljust(23), " ".rjust(20), "|".rjust(6), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 6칸, 구분자없음
    print("| ", "".center(50, '-'), " |")
    # 가운데 정렬 50칸 하이픈으로 채운다.
    time.sleep(0.5)
    # 넘어가는데 0.5초 임의로 딜레이를 준다.
    print("| ".ljust(6), f"Movie  :".ljust(20), f"{rsrvtDB[rsrvt][1]}".rjust(20),"|".rjust(14), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 14칸, 구분자없음
    print("| ".ljust(6), f"Num   :".ljust(20), f"{rsrvtDB[rsrvt][6]}".rjust(20), "|".rjust(15), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 15칸, 구분자없음
    print("| ".ljust(6), f"Area   :".ljust(20), f"{rsrvtDB[rsrvt][8]}".rjust(20), "|".rjust(8), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 8칸, 구분자없음
    time.sleep(0.5)
    # 넘어가는데 0.5초 임의로 딜레이를 준다.
    print("| ".ljust(6), f"Time   :".ljust(20), f"{rsrvtDB[rsrvt][9]}".rjust(20), "|".rjust(14), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 14칸, 구분자없음
    seat_num = 11
    # 좌석정보는 11열부터 나온다.
    for i in range(0, rsrvtDB[rsrvt][6]):
        # 0부터 인원수 - 1 까지 반복한다.
        time.sleep(0.5)
        # 넘어가는데 0.5초 임의로 딜레이를 준다.
        print("| ".ljust(6), f"Seat    :".ljust(20), f"({rsrvtDB[rsrvt][seat_num]})".rjust(20), "|".rjust(17), sep='')
        # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 20칸, 오른쪽정렬 17칸, 구분자없음
        # 좌석정보 reservationDB[reservation][11] 부터 인원수 만큼 순차적으로 출력한다
        seat_num += 1
        # seat_num을 한자리 올려서 반복, 다음 좌석의 열번호이다.
    print("| ", "".center(50, '-'), " |")
    # 가운데 정렬 50칸 하이픈으로 채운다.
    print("| ", "".center(50, '-'), " |")
    # 가운데 정렬 50칸 하이픈으로 채운다.
    print("| ".ljust(6), f"Total       ".ljust(20), f" \ {rsrvtDB[rsrvt][7]}".rjust(19), "|".rjust(14), sep='')
    # 왼쪽정렬 6칸, 왼쪽정렬 20칸, 오른쪽정렬 19칸, 오른쪽정렬 14칸, 구분자없음
    print("| ", "".center(50, '-'), " |")
    # 가운데 정렬 50칸 하이픈으로 채운다.
    time.sleep(0.5)
    # 넘어가는데 0.5초 임의로 딜레이를 준다.
    print("| ", "".center(58, ' '), " |")
    # 공백으로 58칸 가운데정렬
    print("|", "".center(33, 'V'), "|")
    # 33칸 가운데 정렬 나머지는 V로채운다.
    print('\n\n')
    # 두줄띄운다.
    time.sleep(1)
    # 넘어가는데 1초 임의로 딜레이를 준다.
