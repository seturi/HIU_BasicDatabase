/*
  데이터베이스 생성 및 지정
*/
create database IF NOT EXISTS university;
use university;

set foreign_key_checks = 0;   -- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS student cascade;   -- 기존 student 테이블 제거  
drop table IF EXISTS course cascade;   -- 기존 course 테이블 제거  
drop table IF EXISTS enroll cascade;   -- 기존 enroll 테이블 제거  
set foreign_key_checks = 1;   -- 외래키 체크하는 것으로 설정


/*
  student 테이블 생성
*/
create table student (
   sno char(7) NOT NULL, 
   sname varchar(20) NOT NULL, 
	grade int DEFAULT 1, 
	dept varchar(20),
	primary key (sno));

/*
  course 테이블 생성
*/
create table course(
	cno char(4),
	cname varchar(30) not null,
	credit int,
	profname varchar(20),
	dept varchar(20),
       	primary key (cno)
);

/*
  enroll 테이블 생성
*/
create table enroll(
	sno char(15),
	cno char(4),
	lettergrade char(2),
	midterm int,
	final int,
	FOREIGN KEY (sno) REFERENCES student (sno) on delete cascade,
	FOREIGN KEY (cno) REFERENCES course (cno) on delete cascade,
    	primary key (sno, cno)
);

/*
  student 테이블에 샘플 레코드 삽입
*/
insert into student 
values('C090309', '홍길동', 4,'컴퓨터공');
insert into student 
values('C090515', '이순신', 3, '전기공');
insert into student 
values('B990801', '김세종', 3, '전기공');
insert into student 
values('B710628', '김철수', 2, '디자인');
insert into student 
values('B870805', '김영희', 3, '기계공');
insert into student 
values('C170805', '김제주', 2, '산업공');


/*
  course 테이블에 샘플 레코드 삽입
*/
insert into course 
values('C101', 'C프로그래밍', 3, '김대구', '컴퓨터공');
insert into course 
values('C102', 'OS', 3, '이부산', '컴퓨터공');
insert into course 
values('C103', '자료구조', 2, '박광주', '컴퓨터공');
insert into course 
values('C104', '산공개론', NULL, '홍전주', '산업공');


/*
  enroll 테이블에 샘플 레코드 삽입
*/
insert into enroll 
values('C090309', 'C101', 'B', 80 ,80);
insert into enroll 
values('B990801', 'C103', 'C', 80, 75);
insert into enroll 
values('B870805', 'C102', 'A', 100, 85);
insert into enroll 
values('B870805', 'C103', 'A', 90, 90);
insert into enroll 
values('C170805', 'C102', 'B', 95, 80);
insert into enroll 
values('C090515', 'C103', 'B', 80, 95);

-- (1)
/*
	student 테이블의 모든 데이터 검색
*/
select	*
from	student;

/*
	course 테이블의 모든 데이터 검색
*/
select	*
from	course;

/*
	enroll 테이블의 모든 데이터 검색
*/
select	*
from enroll;

-- (2)
/*
	이름이 '자료구조'인 과목을 강의하는 담당교수 이름과 학점 수
*/
select	profname as '담당교수 이름', credit as '학점 수'
from	course
where	cname = '자료구조';


-- (3)
/*
이름이 '김'으로 시작하며 '전기공' 학과에 소속된 학생의 학번과 이름
*/
select	sno as '학번', sname as '이름'
from student
where sname like '김%' and dept = '전기공';

-- (4)
/*
	학점이 입력되어 있지 않은 과목의 이름
*/
select	cname as '과목'
from	course
where	credit is null;

-- (5)
/*
	과목을 개설한 모든 학과 이름 중복 없이 검색
*/
select	distinct dept as "과목 개설한 모든 학과"
from	course;

-- (6)
/*
	'기계공' 학과에 재학중인 학생 수
*/
select	count(dept) as "기계공학과 학생 수"
from	student
where	dept = "기계공";

/*
	모든 재학생의 평균 학년
*/
select	avg(grade) as "재학생 평균 학년"
from	student;

-- (7)
/*
	중간고사 점수가 95점 이하인 학생의 학번과 기말고사 점수
	기말고사 점수로 내림차순, 학번으로 오름차순
*/
select		sno as "학번", final as "기말고사 점수"
from		enroll
where		midterm <= 95
order by	final desc, sno asc;
