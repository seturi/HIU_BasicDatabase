import pymysql

'''
    함수 이름: create_records
    기능: teacher 테이블에 삽입할 레코드를 생성하는 함수로, t_id는 "T1"부터 입력받은 개수의 레코드 수만큼 생성하여 삽입하고,
        t_no는 생성된 t_id의 값을 두번 중복한 문자열을 생성하여 삽입함 
    인자: records_num 삽입하려는 레코드의 개수
    반환값: 없음
'''
def create_records(records_num):
    for i in range(1, records_num + 1):
        t_id = "T" + str(i)
        t_no = t_id * 2
        cursor.execute("insert into teacher values('%s', '%s')" % (t_id, t_no))
        conn.commit()

'''
    메인 함수
'''
# 데이터베이스 접속 및 커서 생성
conn = pymysql.connect(host='localhost', user='root',
                       password='root', db='school', charset='utf8mb4')
cursor = conn.cursor()

# teacher 테이블 생성
cursor.execute("drop table IF EXISTS teacher cascade")
cursor.execute("""
                create table teacher(
                t_id    varchar(10),
                t_no    varchar(30),
                primary key (t_id))
                """)

# 삽입하려는 레코드의 개수를 입력받아 int형으로 변환한다
records_num = int(input("생성할 teacher 테이블의 레코드 수를 입력하시오. : "))

# 레코드 생성
create_records(records_num)

# 데이터베이스 종료
conn.close()