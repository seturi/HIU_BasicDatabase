import pymysql

'''
    함수 이름: set_drop()
    기능: 테이블 초기화 함수
    전달 인자: 없음
    반환값: 없음
'''
def set_drop():
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table IF EXISTS hotel cascade")
    cursor.execute("drop table IF EXISTS hotel_room cascade")
    cursor.execute("drop table IF EXISTS customer cascade")
    cursor.execute("drop table IF EXISTS booking cascade")
    cursor.execute("set foreign_key_checks = 1")


'''
    함수 이름: create_table()
    기능: 호텔, 호텔방, 고객, 예약 테이블을 생성하는 함수
    전달 인자: 없음
    반환값: 없음
'''
def create_table():
    # 호텔 테이블 생성
    cursor.execute("""
        create table hotel(
        HID		varchar(30)	not null,
        호텔이름	varchar(30)	not null,
        호텔주소	varchar(30),
        primary key(HID))""")

    # 호텔방 테이블 생성
    cursor.execute("""
        create table hotel_room(
        HID		varchar(30)	not null,
        호실		varchar(30)	not null,
        가격		int	        default 0,
        primary key(HID, 호실),
        foreign key(HID) references	hotel(HID)
        on delete cascade,
        check(가격 >= 0))""")

    # 고객 테이블 생성
    cursor.execute("""
        create table customer(
        CID			varchar(30)	not null,
        고객이름		varchar(30)	not null,
        고객전화번호	varchar(30),
        primary key(CID))""")

    # 예약 테이블 생성
    cursor.execute("""
        create table booking(
        CID			varchar(30)		not null,
        HID			varchar(30)		not null,
        호실			varchar(30)		not null,
        체크인날짜	varchar(30)     not null,
        체크아웃날짜  varchar(30)	    not null,
        primary key(CID, HID, 호실),
        foreign key(CID) references customer(CID)
        on delete cascade,
        foreign key(HID, 호실) references hotel_room(HID, 호실)
        on delete cascade)""")


'''
    함수 이름: insert_customer()
    기능: 입력 파일로부터 고객 정보를 읽어 고객 테이블에 삽입하고 결과를 출력 파일에 저장하는 함수
    전달 인자: 없음
    반환값: 없음
'''
def insert_customer():
    # 입력 형식: CID, 고객이름, 고객전화번호 정보를 입력 파일로부터 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = column_values[0]
    customer_name = column_values[1]
    customer_phone = column_values[2]

    # 삽입 sql 실행
    sql = "insert into customer values('%s', '%s', '%s')" % (CID, customer_name, customer_phone)
    cursor.execute(sql)

    # 출력 형식
    w_file.write("1.1. 회원가입\n")
    w_file.write("> %s %s %s\n" % (CID, customer_name, customer_phone))


'''
    함수 이름: insert_booking()
    기능: 입력 파일로부터 예약 정보를 읽어 현재 로그인 한 고객의 예약 테이블에 삽입하고, 결과를 출력 파일에 저장하는 함수
    전달 인자: current_CID 현재 로그인한 고객의 ID
    반환값: 없음
'''
def insert_booking(current_CID):
    # 입력 형식: CID, HID, 호실, 체크인날짜, 체크아웃날짜 정보를 입력 파일로부터 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = current_CID
    HID = column_values[0]
    room_num = column_values[1]
    checkin_date = column_values[2]
    checkout_date = column_values[3]

    # 삽입 sql 실행
    sql = ("insert into booking values('%s', '%s', '%s', '%s', '%s')" % (CID, HID, room_num, checkin_date, checkout_date))
    cursor.execute(sql)

    # 출력 형식
    w_file.write("2.2. 호텔방 예약\n")
    w_file.write("> %s %s %s %s\n" % (HID, room_num, checkin_date, checkout_date))


'''
    함수 이름: insert_hotel()
    기능: 입력 파일로부터 호텔 정보를 읽어 호텔 테이블에 삽입하고, 결과를 출력 파일에 저장하는 함수
    전달 인자: 없음
    반환값: 없음
'''
def insert_hotel():
    # 입력 형식: HID, 호텔이름, 호텔주소 정보를 입력 파일로부터 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    HID = column_values[0]
    hotel_name = column_values[1]
    hotel_address = column_values[2]

    # 삽입 sql 실행
    sql = "insert into hotel values('%s', '%s', '%s')" % (HID, hotel_name, hotel_address)
    cursor.execute(sql)

    # 출력 형식
    w_file.write("3.2. 호텔 정보 등록\n")
    w_file.write("> %s %s %s\n" % (HID, hotel_name, hotel_address))


'''
    함수 이름: insert_hotel_room()
    기능: 입력 파일로부터 호텔방 정보를 읽어 호텔방 테이블에 삽입하고, 결과를 출력 파일에 저장하는 함수
    전달 인자: 없음
    반환값: 없음    
'''
def insert_hotel_room():
    # 입력 형식: HID, 호실, 가격 정보를 입력 파일로부터 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    HID = column_values[0]
    room_num = column_values[1]
    price = column_values[2]

    # 삽입 sql 실행
    sql = "insert into hotel_room values('%s', '%s', %s)" % (HID, room_num, price)
    cursor.execute(sql)

    # 출력 형식
    w_file.write("3.3. 호텔방 정보 등록\n")
    w_file.write("> %s %s %s\n" % (HID, room_num, price))


'''
    함수 이름: select_booking()
    기능: 현재 로그인한 고객의 예약 내역을 조회해 결과를 파일에 출력하는 함수
    전달 인자: current_CID 현재 로그인한 고객 ID
    반환값: 없음
'''

def select_booking_customer(current_CID):
    w_file.write("2.3. 호텔방 예약 조회\n")

    # 검색 sql 실행
    sql = "select * from booking where CID = '%s'" % current_CID
    cursor.execute(sql)
    rows = cursor.fetchall()

    if not rows:    # 검색된 레코드가 없는 경우
        w_file.write("> \n")
        return
    else:           # 있는 경우, 검색 결과 레코드 출력 파일에 저장
        for cur_row in rows:
            HID = cur_row[1]
            hotel_num = cur_row[2]
            checkin_date = cur_row[3]
            checkout_date = cur_row[4]
            w_file.write("> %s %s %s %s \n" % (HID, hotel_num, checkin_date, checkout_date))

'''
    함수 이름: delete_booking()
    기능: 현재 로그인한 고객의 예약 내역 중 입력 파일로부터 HID와 호실을 읽어 해당되는 예약을 취소하는 함수
    전달 인자: current_CID 현재 로그인한 고객 ID
    반환값: 없음
'''
def delete_booking(current_CID):
    w_file.write("2.4. 호텔방 예약 취소\n")

    # 입력 파일로부터 취소 하려는 예약 정보 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = current_CID
    HID = column_values[0]
    room_num = column_values[1]

    # 삭제 sql문
    sql = """
            delete from booking 
            where   CID = '%s'
            and     HID = '%s'
            and     호실 = '%s'
            """ % (CID, HID, room_num)

    try:                        # 삭제 sql문 실행
        cursor.execute(sql)
        w_file.write("> %s %s\n" % (HID, room_num))
    except Exception as error:  # 예외 처리: 에러 메시지 출력
        print(error)


'''
    함수 이름: select_booking_admin()
    기능: 관리자 권한으로 모든 고객들의 예약 내역을 조회해 결과를 파일에 출력하는 함수 
    전달 인자: current_CID 현재 로그인한 고객 ID
    반환값: 없음
'''
def select_booking_admin():
    w_file.write("3.4. 예약 내역 조회\n")

    # 모든 고객의 예약 정보를 검색하는 sql문
    sql = ("""
            select  b.CID, c.고객이름, b.HID, h.호텔이름, h.호텔주소, b.호실, r.가격, b.체크인날짜, b.체크아웃날짜 
            from    booking b, hotel h, customer c, hotel_room r
            where   b.CID = c.CID
            and     b.HID = h.HID
            and     b.호실 = r.호실
            and     b.HID = r.HID
            """)

    # 검색 sql문 실행
    cursor.execute(sql)
    rows = cursor.fetchall()

    if not rows:    # 검색된 레코드가 없는 경우
        w_file.write("> \n")
    else:           # 검색 결과 레코드 출력 파일에 저장
        for cur_row in rows:
            CID = cur_row[0]
            customer_name = cur_row[1]
            HID = cur_row[2]
            hotel_name = cur_row[3]
            hotel_address = cur_row[4]
            room_num = cur_row[5]
            price = cur_row[6]
            checkin_date = cur_row[7]
            checkout_date = cur_row[8]

            # 출력 형식
            w_file.write("> %s %s %s %s %s %s %s %s %s \n"
                         % (CID, customer_name, HID, hotel_name, hotel_address, room_num, price, checkin_date, checkout_date))

'''
    함수 이름: exit()
    기능: 프로그램을 종료하기 위해 결과 파일에 문구를 출력하는 함수
    전달 인자: 없음
    반환값: 없음
'''
def exit():
    w_file.write("1.2. 종료")


'''
    함수 이름: login()
    기능: 입력 파일로부터 현재 로그인하려는 고객(관리자)의 ID를 읽고, 메뉴 레벨에 따라 
        일반 고객 또는 관리자로 로그인했음을 결과 파일에 출력하는 함수
    전달 인자: menu_level_1이 2면 일반 고객 권한으로 로그인, 3이면 관리자 권한
    반환값: current_CID 현재 로그인한 고객(관리자) ID
'''
def login(menu_level_1):
    # 현재 로그인하려는 고객의 ID 읽기
    current_CID = r_file.readline().strip()

    # 일반 고객으로 로그인하려는 경우
    if menu_level_1 == 2:
        w_file.write("2.1. 로그인\n")
        w_file.write("> %s\n" % current_CID)

    # 관리자로 로그인하려는 경우
    elif menu_level_1 == 3:
        w_file.write("3.1. 로그인\n")
        w_file.write("> %s\n" % current_CID)

    return current_CID


'''
    함수 이름: logout()
    기능: 현재 로그인한 고객(관리자)이 로그아웃했음을 결과 파일에 출력하는 함수
    전달 인자: menu_level_1이 2면 일반 고객 권한, 3이면 관리자 권한, current_CID 현재 로그인한 고객(관리자) ID
    반환값: 없음
'''
def logout(menu_level_1, current_CID):
    # 일반 고객으로 로그인한 경우
    if menu_level_1 == 2:
        w_file.write("2.5. 로그아웃\n")
        w_file.write("> %s\n" % current_CID)

    # 관리자로 로그인한 경우
    elif menu_level_1 == 3:
        w_file.write("3.5. 로그아웃\n")
        w_file.write("> %s\n" % current_CID)


'''
    함수 이름: do_task()
    기능: 입력 파일을 읽어 메뉴에 따라 해당되는 작업을 수행하는 함수, 종료 메뉴가 선택되면 종료 
    전달 인자: 없음
    반환값: 없음
'''
def do_task():
    # 종료 메뉴 "1 2"가 입력 되기 전까지 반복
    while True:
        # 입력 파일에서 메뉴 숫자 2개 읽기
        line = r_file.readline()
        line = line.strip()
        menu_levels = line.split()

        # 메뉴 파싱을 위한 level 구분
        menu_level_1 = int(menu_levels[0])
        menu_level_2 = int(menu_levels[1])

        # 메뉴 구분 및 해당 연산 수행
        if menu_level_1 == 1:
            # 1.1. 회원가입
            if menu_level_2 == 1:
                insert_customer()

            # 1.2. 종료
            elif menu_level_2 == 2:
                exit()
                break

        elif menu_level_1 == 2:
            # 2.1. 로그인
            if menu_level_2 == 1:
                current_CID = login(2)

            # 2.2. 호텔방 예약
            elif menu_level_2 == 2:
                insert_booking(current_CID)

            # 2.3. 호텔방 예약 조회
            elif menu_level_2 == 3:
                select_booking_customer(current_CID)

            # 2.4. 호텔방 예약 취소
            elif menu_level_2 == 4:
                delete_booking(current_CID)

            # 2.5. 로그아웃
            elif menu_level_2 == 5:
                logout(2, current_CID)

        elif menu_level_1 == 3:
            # 3.1 로그인(admin)
            if menu_level_2 == 1:
                current_CID = login(3)

            # 3.2 호텔 정보 등록
            elif menu_level_2 == 2:
                insert_hotel()

            # 3.3 호텔방 정보 등록
            elif menu_level_2 == 3:
                insert_hotel_room()

            # 3.4 예약 내역 조회
            elif menu_level_2 == 4:
                select_booking_admin()

            # 3.5 로그아웃
            elif menu_level_2 == 5:
                logout(3, current_CID)


'''
----------------
    메인 함수
----------------
'''
# 데이터베이스 접속 및 커서 생성
conn = pymysql.connect(host = 'localhost', user = 'root',
    password = 'root', db ='hotel_booking', charset = 'utf8mb4')
cursor = conn.cursor()

# 기존 테이블 삭제
set_drop()

# input 파일 읽어 오고 출력 결과를 output 파일에 저장
r_file = open("input.txt", "r", encoding='utf-8')
w_file = open("output.txt", "w", encoding='utf-8')


# 호텔, 호텔방, 고객, 예약 테이블 생성
create_table()

# input 파일을 읽어 메뉴에 따라 작업 수행
do_task()

# 기존 테이블 삭제
set_drop()

# input, output 파일 닫기
r_file.close()
w_file.close()

# 데이터베이스 접속 종료
conn.close()