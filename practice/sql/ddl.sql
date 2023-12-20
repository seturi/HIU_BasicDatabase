-- 데이터베이스 생성 및 지정
create database IF NOT EXISTS university;
use university;

-- 기존 테이블 제거
drop table IF EXISTS students;

-- 학생 테이블 생성
create table student (
	sno   char(7)     NOT NULL,
    sname varchar(20) NOT NULL,
    grade int default 1,
	dept  varchar(20),
    primary key(sno)
);

-- 현재 DB에 정의된 모든 테이블(학생 테이블) 출력
show tables;

-- 학생 테이블의 모든 column 정보 출력
desc student;

-- 주소 column 추가
alter table student
	add address varchar(30);
desc student;

-- 주소 column 삭제
alter table student drop column address;
desc student;

-- 학생 테이블 삭제
drop table student;
show tables
