import pymysql

'''
    테이블 초기화 함수
'''
def set_drop():
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table IF EXISTS student cascade")
    cursor.execute("drop table IF EXISTS course cascade")
    cursor.execute("drop table IF EXISTS enroll cascade")
    cursor.execute("set foreign_key_checks = 1")

'''
    기능: 입력 값에 따라 student 또는 course 레코드를 삽입하는 sql 생성 함수
    인자: '1'이면 student 레코드 삽입, '2'이면 course 레코드 삽입
'''
def insert_table(switch):
    sql = "insert into "

    # 1을 입력한 경우: student 레코드 삽입
    if switch == '1':
        sno = input('학번 : ')
        sname = input("이름: ")
        grade = input("학년: ")
        dept = input("학과: ")
        sql += "student values('" + sno + "', '" + sname + \
                "', " + grade + ", '" + dept + "')"

    # 2를 입력한 경우: course 레코드 삽입
    elif switch == '2':
        cno = input('과목번호 : ')
        cname = input("과목이름: ")
        credit = input("학점: ")
        profname = input("담당교수: ")
        dept = input("담당학과: ")

        sql += "course values('" + cno + "', '" + cname + \
                "', " + credit + ", '" + profname + "', '" + dept + "')"

    return sql

'''
    기능: 입력 값에 따라 student 또는 course 레코드를 검색하는 sql 생성 함수
    인자: '3'이면 student 레코드를, '4'이면 course 레코드 검색
'''
def select_table(switch):
    sql = 'select * from '

    # 3을 입력한 경우: student 레코드 출력
    if switch == '3':
        sql += 'student'

    # 4를 입력한 경우: course 레코드 출력
    elif switch == '4':
        sql += 'course'

    return sql

'''
    기능: 입력값에 따라 student 또는 course 레코드 검색 결과 출력하는 함수
    인자: switch가 '3'이면 student, '4'이면 course 출력 
'''
def print_table(cursor, switch):
    sql = select_table(switch)
    if switch == '3':
        print("%7s %20s %5s %20s" % ("학번", "이름", "학년", "학과"))

        cursor.execute(sql)
        rows = cursor.fetchall()
        for cur_row in rows:
            sno = cur_row[0]
            sname = cur_row[1]
            grade = cur_row[2]
            dept = cur_row[3]
            print("%7s %20s %5d %20s" % (sno, sname, grade, dept))

    elif switch == '4':
        print("%4s %30s %5s %20s %20s" % ("과목번호", "과목이름", "학점", "담당교수", "학과"))

        cursor.execute(sql)
        rows = cursor.fetchall()
        for cur_row in rows:
            cno = cur_row[0]
            cname = cur_row[1]
            credit = cur_row[2]
            profname = cur_row[3]
            dept = cur_row[4]
            print("%7s %20s %5d %20s %20s" % (cno, cname, credit, profname, dept))


conn = pymysql.connect(host='localhost', user='root',
                       password='root', db='university', charset='utf8mb4')

cursor = conn.cursor()

set_drop()
'''
    student 테이블 생성
'''
cursor.execute("create table student(\
    sno char(7) NOT NULL, \
    sname varchar(20) NOT NULL,\
    grade int DEFAULT 1, \
	dept varchar(20),\
	primary key (sno))")

'''
    course 테이블 생성
'''
cursor.execute("create table course(\
    cno char(4),\
	cname varchar(30) not null,\
	credit int,\
    profname varchar(20),\
	dept varchar(20),\
    primary key (cno));")

'''
    입력값에 따라 레코드 삽입 또는 검색, 또는 프로그램 종료
    0을 입력받을 때까지 계속 수행
'''
while(True):
    print("0: 종료")
    print("1: student 레코드 삽입")
    print("2: course 레코드 삽입")
    print("3: student 레코드 검색")
    print("4: course 레코드 검색")

    input_num = input("기능을 선택하시오 : ")
    if(input_num == '0'):   # 종료
        break

    elif(input_num == '1' or input_num == '2'):
        cursor.execute(insert_table(input_num))

    elif(input_num == '3' or input_num == '4'):
        print_table(cursor, input_num)

    else:
        print("0 ~ 4 사이의 숫자만 입력하세요.")

set_drop()
conn.close()

