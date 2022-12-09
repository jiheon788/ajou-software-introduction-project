## MovieReservationProject/cinemapps/admin.py
from random import  *
# 랜덤패키지를 모두 import한다.

#########################
ADMIN_PASSWORD = 12345678
#########################
## ############관리자 비밀번호
# ###########상수로 설정해둔다.

def print_admin_channel():
    # 함수정의, 매개변수x, 반환값x
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
    print("*                Admin Channel                  *")
    print("*                  ----------------                  *")
    print("*                                                       *")
    print("*   1. DB 출력                                      *")
    print("*   2. DB 저장                                      *")
    print("*                                                       *")
    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")

def print_system_message(message):
    # 함수정의, 매개변수로 메시지를 받는다.
    print(f"\n====================\nSystem: {message}\n====================\n")
    #메시지를 특정형식으로 출력한다. 시스템 메시지 출력용

def generate_code():
    # 반환값만 있는 함수 정의
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    # 알파벳과 숫자 문자열
    code = ""
    # 빈문자열 정의
    for i in range(6):
        # 0부터 5까지 총 6번 반복
        index = randrange(len(alphabet))
        # 0부터 알파벳변수의 길이까지의 랜덤한정수를 뽑아 인덱스로 만든다.
        code += alphabet[index]
        # code에 해당인덱스를 가지 문자를 할당한다.
    return code
    # code를 반환한다.

def customer_login(athntCode):
    # 인증코드를 매개변수로 받는다.
    for i in range(3):
        #0 ~ 2까지, 세번 반복한다.
        inputCode = input(f"인증코드를 입력하세요({3 - i}/3): ")
        # 인증코드를 입력받아 문자열 그대로 할당, 남은 로그인시도 횟수를 보여준다.
        if inputCode != athntCode:
            # 입력한 코드가 다르면 안내문 출력한다.
            print("인증실패. ")
            if (3 - i) == 1:
            # i가 2가 되었을떄 = 기회를 세번 모두 썻을 떄
                return False
                # False 반환 > 로그인 실패
            else:
            # 아직 기회가 남아있으면
                continue
                # 다시 반복
        elif inputCode == athntCode:
            #입력한 코드가 맞으면
            return True
            # True 반환 > 인증완료

def admin_login():
    # 함수 정의, 로그인
    for i in range(3):
        #0 ~ 2까지, 세번 반복한다.
        inputPW = int(input(f"패스워드를 입력하세요({3 - i}/3): "))
        # 패스워드를 입력받고 정수로 형변환 후 할당, 남은 로그인시도 횟수를 보여준다.
        if inputPW != ADMIN_PASSWORD:
            # 입력한 비밀번호가 다르면 안내문 출력한다.
            print("틀렸습니다. ")
            if (3 - i) == 1:
                # i가 2가 되었을떄 = 기회를 세번 모두 썻을 떄
                return False
                # False 반환 > 로그인 실패
            else:
                # 아직 기회가 남아있으면
                continue
                # 다시 반복
        elif inputPW == ADMIN_PASSWORD:
            #입력한 비밀번호가 맞으면
            return True
            # True 반환 > 로그인 성공