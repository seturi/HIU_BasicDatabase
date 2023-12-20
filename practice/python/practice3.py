import pymysql

'''
    함수 이름: set_drop()
    기능: 테이블 초기화 함수
    전달 인자: 없음
    반환값: 없음
'''
def set_drop():
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table IF EXISTS student cascade")
    cursor.execute("drop table IF EXISTS course cascade")
    cursor.execute("drop table IF EXISTS enroll cascade")
    cursor.execute("set foreign_key_checks = 1")

'''
    함수 이름: select_table()
    기능: 입력 값에 따라 student 또는 course 레코드를 검색하는 sql 생성 함수
    전달 인자: switch 값이 1이면 student, 2이면 course, 3이면 enroll 레코드 검색
    반환값: sql문 문자열
'''
def select_table(switch):
    sql = 'select * from '

    # 1: student 레코드 검색 sql 생성
    if switch == 1:
        sql += 'student'

    # 2: course 레코드 검색 sql 생성
    elif switch == 2:
        sql += 'course'

    # 3: enroll 레코드 검색 sql 생성
    elif switch == 3:
        sql += 'enroll'

    return sql

'''
    함수 이름: print_table()
    기능: 입력 값에 따라 student 또는 course 또는 enroll 레코드를 검색한 결과를 출력하는 함수
    전달 인자: switch가 1이면 student, 2면 course, 3이면 enroll 레코드 검색 결과 출력
    반환값: 없음 
'''
def print_table(switch):
    sql = select_table(switch)  # switch에 따라 select_table 함수로 sql 생성

    # student 레코드 검색 결과 출력
    if switch == 1:
        w_file.write("1. student 레코드 검색\n")

        cursor.execute(sql)
        rows = cursor.fetchall()
        for cur_row in rows:
            sno = cur_row[0]
            sname = cur_row[1]
            grade = str(cur_row[2])
            dept = cur_row[3]
            w_file.write("%s %s %s %s\n" % (sno, sname, grade, dept))

    # course 레코드 검색 결과 출력
    elif switch == 2:
        w_file.write("2. course 레코드 검색\n")

        cursor.execute(sql)
        rows = cursor.fetchall()
        for cur_row in rows:
            cno = cur_row[0]
            cname = cur_row[1]
            credit = str(cur_row[2])
            profname = cur_row[3]
            dept = cur_row[4]
            w_file.write("%s %s %s %s %s\n" % (cno, cname, credit, profname, dept))

    # enroll 레코드 검색 결과 출력
    elif switch == 3:
        w_file.write("3. enroll 레코드 검색\n")

        cursor.execute(sql)
        rows = cursor.fetchall()
        for cur_row in rows:
            sno = cur_row[0]
            cno = cur_row[1]
            final = str(cur_row[2])
            lettergrade = cur_row[3]
            w_file.write("%s %s %s %s\n" % (sno, cno, final, lettergrade))

'''
    함수 이름: insert_enroll()
    기능: enroll 레코드를 삽입하는 sql을 실행하는 함수
    전달 인자: list 형으로 된 삽입하려는 enroll 레코드
    반환값: 없음
'''
def insert_enroll(records):
    w_file.write("4. enroll 레코드 삽입\n")

    sno= records[0]
    cno = records[1]
    final = records[2]
    lettergrade = records[3]

    sql = "insert into enroll values('" + sno + "', '" + cno + \
            "', " + final + ", '" + lettergrade + "')"

    cursor.execute(sql)
    w_file.write("%s %s %s %s\n" % (sno, cno, final, lettergrade))

'''
    메인 함수
'''

# 데이터베이스 접속 및 커서 생성
conn = pymysql.connect(host = 'localhost', user = 'root',
    password = 'root', db ='university', charset = 'utf8mb4')
cursor = conn.cursor()

# 기존 테이블 삭제
set_drop()

# student 테이블 생성
cursor.execute("create table student(\
    sno char(7) NOT NULL, \
    sname varchar(20) NOT NULL,\
    grade int DEFAULT 1, \
	dept varchar(20),\
	primary key (sno))")

# course 테이블 생성
cursor.execute("create table course(\
    cno char(4),\
	cname varchar(30) not null,\
	credit int,\
    profname varchar(20),\
	dept varchar(20),\
    primary key (cno));")

# enroll 테이블 생성
cursor.execute("create table enroll(\
	sno char(7),\
	cno char(4),\
    final int,\
	lettergrade char(2),\
    primary key (sno, cno))")

# student 레코드 삽입
cursor.execute("insert into student values('B922019', '김영희', 4, '기계')")
cursor.execute("insert into student values('B990617', '홍철수', 3, '컴퓨터')")

# course 레코드 삽입
cursor.execute("insert into course values('C101', '동역학', 3, '김공과', '기계')")
cursor.execute("insert into course values('C102', '데이터베이스', 4, '유대학', '컴퓨터')")

# input 파일 읽어 오고 출력 결과를 output 파일에 저장
r_file = open("input.txt", "r")
w_file = open("output.txt", "w")

while True:
    # input 파일의 한 행을 읽는다
    line = r_file.readline()
    if not line:    # 빈 경우 종료
        break

    # 입력받은 숫자를 메뉴를 스위치하는 번호로 사용하기 위해 int로 변환
    input_switch = int(line)

    # 0인 경우: 종료
    if input_switch == 0:
        w_file.write("0. 종료\n")
        break

    # 1 ~ 3인 경우: 각각의 레코드 검색
    elif 1 <= input_switch <= 3:
        print_table(input_switch)

    # 4인 경우: enroll 레코드 삽입
    elif input_switch == 4:
        # 다음 행을 읽어 해당 데이터 삽입
        line = r_file.readline()
        line = line.strip()
        column_values = line.split()
        insert_enroll(column_values)

# 기존 테이블 삭제
set_drop()

# input, output 파일 닫기
r_file.close()
w_file.close()

# 데이터베이스 접속 종료
conn.close()