import pymysql


# 함수 이름 : select_student()
# 기능 : 모든 student 레코드를 검색한 후 출력함
# 반환값 : 없음
# 전달인자 : 없음
def select_student():
    print(">> student 레코드 검색 결과")
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for cur_row in rows:
        sno = cur_row[0]
        sname = cur_row[1]
        grade = cur_row[2]
        dept = cur_row[3]
        print(sno + ' ' + sname + ' ' + str(grade) + ' ' + dept)


# 함수 이름 : insert_student()
# 기능 : 키보드로부터 속성들을 입력받아서 student 레코드를 삽입함
# 반환값 : 입력받은 값으로 작성한 insert 문장
# 전달인자 : 없음
def insert_student():
    print(">> student 레코드 삽입")
    sno = input("학번: ")
    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    if sno == "" :
        sql = "insert into student values(NULL, '" + sname + "', " + grade + ", '" + dept + "')"
    else :
        sql = "insert into student values('" + sno + "', '" + sname + "', " + grade + ", '" + dept + "')"

    return sql


# 함수 이름 : execute_transaction()
# 기능 :학생 레코드의 grade 값을 1씩 증가시키고, 새로운 레코드를 삽입하는 sql 전체를 트랜잭션으로 처리한다.
#       start transaction을 통해 새로운 트랜잭션의 시작을 알리고,
#       try문에서 update문과 insert문(insert_sql 함수 이용)을 트랜잭션으로 처리해 수행함.
#       에러가 발생할 시 except문에서 만약에 실행 됐을 sql문에 대해 rollback 연산을 해서 아무것도
#       발생하지 않은 것처럼 처리해 DB 전체가 일관된 상태가 되게 하고 에러문 출력함
#       이 문제의 경우, 삽입하려는 레코드의 학번이 NULL일 때 에러가 발생하여 수행됐을 update문에 대해 rollback 처리됨
# 반환값 : 없음
# 전달인자 : 없음
def execute_transaction():

    insert_sql = insert_student()

    cursor.execute("set autocommit = off")
    cursor.execute("start transaction")

    try:
        sql = """update student 
                set grade = grade + 1"""
        cursor.execute(sql)
        print(insert_sql)
        cursor.execute(insert_sql)
        cursor.execute("commit")
        print('Transaction was executed succesfully !')

    except Exception as error:
        cursor.execute("rollback")
        print(error)
        print('Transaction failed !')

    cursor.execute("set autocommit = on")



##############
#  메인 코드  #
##############

# 데이터베이스 접속 및 커서 생성
conn = pymysql.connect(host='localhost', user='root', password='root', db='university', charset='utf8mb4')
cursor = conn.cursor()

# 기존 테이블 삭제
cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table IF EXISTS student")
cursor.execute("set foreign_key_checks = 1")

# student 테이블 생성
cursor.execute('''create table student(
                sno     char(7) not null,
                sname   varchar(20),
                grade   int,
                dept    varchar(20),
                primary key(sno)
                )''')


# student 레코드 하드코딩으로 삽입
cursor.execute('''insert into student
                  values('B922019', '김영희', 1,'기계')''')
cursor.execute('''insert into student
                  values('B990617', '홍철수', 3,'컴퓨터')''')

# 기존 student 레코드 출력
select_student()

# 트랜잭션을 수행 후 모든 student 레코드 출력
execute_transaction()
select_student()
