## MovieReservationProject/cinemapps/__init__.py
# cinemapps 패키지의 초기화파일
# main.py 에서 cinemaapps패키지를 import 하면 제일 먼저 이 파일을 열어 아래 코드를 읽는다.
# from A.a import * : A폴더의 a파일로부터 모두 import 한다.
from utils.reservation import *
# cinamapps 패키지의 reservation모듈로부터 전부 import 한다.
from utils.theater import *
# cinamapps 패키지의 theater모듈로부터 전부 import 한다.
from utils.admin import *
# cinamapps 패키지의 admin모듈로부터 전부 import 한다.
from utils.payment import *
# cinamapps 패키지의 payment모듈로부터 전부 import 한다.
