-- 데이터베이스 생성 및 지정
create database IF NOT EXISTS hotel_booking;
use hotel_booking;
alter database hotel_booking default character set utf8mb4;

set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정

-- (1)  테이블 생성 
create table hotel(
	HID			char(4)		not null,
    호텔이름		varchar(10)	not null,
    호텔주소		varchar(30),
    호텔전화번호	varchar(20),
    primary key(HID)
);

create table hotelier(
	HLID		char(5)		not null,
    호텔리어이름	varchar(10)	not null,
    HID			char(4),
    primary key(HLID),
    foreign key(HID)
    references	hotel(HID)
    on delete cascade
);

create table hotel_room(
	HID		char(4)		not null,
	호실		char(2)		not null,
    가격		int			default 0,
    primary key(HID, 호실),
    foreign key(HID) 
    references	hotel(HID)
    on delete cascade,
    check(가격 >= 0)
);

create table customer(
	CID			char(4)		not null,
    고객이름		varchar(10)	not null,
    고객전화번호	varchar(20),
    primary key(CID)
);

create table booking(
	CID				char(4)		not null,
    HID				char(4)		not null,
    호실				char(2)		not null,
    예약체크인날짜		char(10)	not null,
    예약체크아웃날짜		char(10)	not null,
    primary key(CID, HID, 호실),
    foreign key(CID)
    references customer(CID)
    on delete cascade,
    foreign key(HID, 호실) 
    references hotel_room(HID, 호실)
    on delete cascade
);

create table stay_information(
	CID			char(4)		not null,
    HID			char(4)		not null,
    호실			char(2)		not null,
    체크인날짜		char(10)	not null,
    체크아웃날짜	char(10)	not null,
    primary key(CID, HID, 호실, 체크인날짜),
    foreign key(CID) 
    references customer(CID)
    on delete cascade,
    foreign key(HID, 호실) 
    references hotel_room(HID, 호실)
    on delete cascade
);

-- (2)  데이터 삽입
-- hotel 데이터 삽입
insert
into	hotel(HID, 호텔이름, 호텔주소, 호텔전화번호)
values	('H001', '홍익호텔', '마포구 상수동', '02-320-1234');
insert
into	hotel(HID, 호텔이름, 호텔주소, 호텔전화번호)
values	('H002', '중앙호텔', '동작구 흑석동', '02-850-1234');
insert
into	hotel(HID, 호텔이름, 호텔주소, 호텔전화번호)
values	('H003', '건국호텔', '광진구 자양동', '02-415-1234');

-- hotelier 데이터 삽입
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL001', 'KMS', 'H001');
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL002', 'LED', 'H001');
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL003', 'YHD', 'H002');
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL004', 'KKT', 'H002');
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL005', 'CPC', 'H003');
insert
into	hotelier(HLID, 호텔리어이름, HID)
values	('HL006', 'LSY', 'H003');

-- hotel_room 데이터 삽입
insert
into	hotel_room(HID, 호실, 가격)
values	('H001', '01', 1400);
insert
into	hotel_room(HID, 호실, 가격)
values	('H001', '02', 1200);
insert
into	hotel_room(HID, 호실, 가격)
values	('H001', '03', 700);
insert
into	hotel_room(HID, 호실, 가격)
values	('H002', '01', 1900);
insert
into	hotel_room(HID, 호실, 가격)
values	('H002', '02', 1000);
insert
into	hotel_room(HID, 호실, 가격)
values	('H002', '03', 1300);
insert
into	hotel_room(HID, 호실, 가격)
values	('H002', '04', 1600);
insert
into	hotel_room(HID, 호실, 가격)
values	('H003', '01', 900);
insert
into	hotel_room(HID, 호실, 가격)
values	('H003', '02', 1100);

-- customer 데이터 삽입
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C001', 'PDN', '010-3304-6302');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C002', 'KYS', '010-7323-3789');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C003', 'YDJ', '010-2628-7436');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C004', 'KSM', '010-2299-7827');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C005', 'PJH', '010-3157-2501');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C006', 'HBC', '010-2936-5427');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C007', 'KCY', '010-7119-6732');
insert
into	customer(CID, 고객이름, 고객전화번호)
values	('C008', 'PYS', '010-2523-9738');

-- booking 데이터 삽입
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C001', 'H001', '01', '2023/07/16', '2023/07/28');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C002', 'H001', '02', '2023/07/21', '2023/07/22');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C001', 'H002', '01', '2023/08/16', '2023/08/18');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C005', 'H002', '01', '2023/09/06', '2023/09/09');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C005', 'H002', '02', '2023/09/10', '2023/09/18');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C003', 'H002', '02', '2023/09/14', '2023/10/17');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C002', 'H002', '03', '2023/10/16', '2023/10/18');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C008', 'H003', '01', '2023/10/22', '2023/10/26');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C004', 'H003', '01', '2023/10/28', '2023/11/02');
insert
into	booking(CID, HID, 호실, 예약체크인날짜, 예약체크아웃날짜)
values	('C003', 'H003', '02', '2023/10/29', '2023/11/03');

-- stay_information 데이터 삽입
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C002', 'H002', '01', '2021/07/16', '2021/07/20');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C001', 'H003', '02', '2021/07/21', '2021/07/25');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C001', 'H001', '01', '2021/08/16', '2021/08/28');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C004', 'H002', '02', '2021/09/06', '2021/09/18');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C001', 'H002', '02', '2021/09/10', '2021/09/17');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C003', 'H002', '02', '2021/09/14', '2021/09/21');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C002', 'H001', '03', '2022/10/15', '2022/10/24');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C005', 'H003', '01', '2022/10/19', '2022/10/26');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C004', 'H002', '01', '2022/10/22', '2022/10/26');
insert
into	stay_information(CID, HID, 호실, 체크인날짜, 체크아웃날짜)
values	('C005', 'H003', '02', '2022/10/29', '2022/11/01');


-- (3)
select "1)";       -- 1) 각 테이블의 모든 레코드 검색

select * from hotel; 			-- 호텔 테이블
select * from hotelier;			-- 호텔리어 테이블
select * from hotel_room;		-- 호텔방 테이블
select * from customer;			-- 고객 테이블
select * from booking;			-- 예약 테이블
select * from stay_information;	-- 투숙 테이블

select "2)";       -- 2) ID가 'H001'인 호텔에서 근무하는 호텔리어의 ID와 이름 검색

select	HLID, 호텔리어이름
from	hotelier
where	HID='H001';

select "3)";       -- 3) 고객별로 자신이 투숙했던 모든 호텔별로 투숙 일 수의 합 검색

select		CID, HID, sum(datediff(
						str_to_date(체크아웃날짜, '%Y/%m/%d'), 
						str_to_date(체크인날짜, '%Y/%m/%d'))) as '투숙 일 수의 합'
from		stay_information
group by	CID, HID;

select "4)";       -- 4) 호텔 예약 중 일 수가 4일 미만인 예약 정보에 대해 고객 이름과 호텔 이름 검색

select	c.고객이름, h.호텔이름
from	booking b, customer c, hotel h
where	datediff(
			str_to_date(b.예약체크아웃날짜, '%Y/%m/%d'), 
			str_to_date(b.예약체크인날짜, '%Y/%m/%d')
            ) < 4
and		c.CID = b.CID
and		h.HID = b.HID;

select "5)";       -- 5) ID가 'C001'인 고객들이 투숙한 총 일 수 검색

select sum(datediff(
			str_to_date(체크아웃날짜, '%Y/%m/%d'), 
			str_to_date(체크인날짜, '%Y/%m/%d')
			)) as '투숙한 총 일 수'
from	stay_information
where	CID = 'C001';

select "6)";       -- 6) 가격이 1300원 이상인 호텔방을 호텔ID에 대해 내림차순으로 호실에 대해 오름차순으로 검색

select		*
from		hotel_room
where		가격 >= 1300
order by	HID desc,	호실 asc;

select "7)";       -- 7) 가장 오래전의 투숙정보를 보유 중인 호텔의 이름과 전화번호 검색

select	h.호텔이름, h.호텔전화번호
from	stay_information s, hotel h
where	s.HID = h.HID
and		s.체크인날짜 <= ALL(
					select	체크인날짜
                    from	stay_information);

select "8)";       -- 8) ID가 'H003'인 호텔이 보유하고 있는 호텔방을 예약한 적이 있는 고객의 이름 검색

select	c.고객이름
from	customer c, booking b
where	b.HID = 'H003'
and		c.CID = b.CID;

select "9)";       -- 9) 체크인 날짜가 2021년인 투숙 정보를 2개 이상 보유 중인 호텔의 이름 검색

select		h.호텔이름
from		hotel h, stay_information s
where		s.체크인날짜 like '2021/__/__'
and			h.HID = s.HID
group by	h.HID	having count(*) >= 2;

select "10)";       -- 10) 2022년 8월 30일 이전에 체크인해서 투숙했던 정보 중에서 주소가 '흑석동'인 호텔을 예약했던 고객의 이름과 전화번호 검색

select	c.고객이름, c.고객전화번호
from	customer c, hotel h, stay_information s
where	c.CID = s.CID
and		h.HID = s.HID
and		str_to_date(s.체크인날짜, '%Y/%m/%d') < '2022-08-30'
and		s.CID in (
					select	b.CID
					from	booking b, hotel h
					where	b.HID = h.HID
					and		h.호텔주소 like '%흑석동%'
				);

select "11)";       -- 11) ID가 'H001'과 'H002'인 호텔을 모두 예약한 적이 있는 고객의 이름 검색

select	c.고객이름
from	customer c, booking b
where	b.HID = 'H001'
and		c.CID = b.CID
and		exists(
		select	*
		from	booking
        where	HID = 'H002');

select "12)";       -- 12) 호텔별로 총 예약 수와 투숙 수 검색

select		HID, count(*) as '총 예약 수'
from		booking
group by	HID;
select		HID, count(*) as '총 투숙 수'
from		stay_information
group by	HID;

select "13)";       -- 13) ID가 'C002'인 고객이 예약한 호텔방의 가격을 모두 100원씩 증가. '호텔방' 테이블의 모든 레코드 검색

update	hotel_room
set		가격 = 가격 + 100
where	(HID, 호실) in (
				select	HID, 호실
				from	booking
                where	CID = 'C002'
                );

select	* from	hotel_room;

select "14)";       -- 14) '중앙호텔'에 근무하는 모든 호텔리어들을 삭제하고 '호텔리어'테이블의 모든 레코드를 검색

delete
from	hotelier
where	HID = (
				select	HID
				from	hotel
				where	호텔이름='중앙호텔'
				);
                
select * from hotelier;

select "15)";       -- 15) 
/*
	'홍익호텔'에 투숙한 경험이 있는 모든 고객들의 ID, 이름 및 전화번호 정보로
    'hongik_hotel_customers'이라는 이름의 뷰를 생성하여 구성, 검색
*/

create view	hongik_hotel_customers(CID,  고객이름, 고객전화번호)
as	select	c.CID, c.고객이름, c.고객전화번호
	from	customer c, hotel h, stay_information s
    where	c.CID = s.CID
    and		h.HID = s.HID
    and		h.호텔이름 = '홍익호텔'
with check option;

select * from hongik_hotel_customers;


set foreign_key_checks = 0;    			-- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS hotel cascade;   				-- 기존 hotel 테이블 제거
drop table IF EXISTS hotelier cascade;   			-- 기존 hotelier 테이블 제거
drop table IF EXISTS hotel_room cascade;   			-- 기존 hotel_room 테이블 제거
drop table IF EXISTS customer cascade;   			-- 기존 customer 테이블 제거
drop table IF EXISTS booking cascade;   			-- 기존 booking 테이블 제거 
drop table IF EXISTS stay_information cascade; 		-- 기존 stay_information 테이블 제거 
drop view IF EXISTS hongik_hotel_customers cascade; -- 기존 hongik_hotel_customers 뷰 제거
set foreign_key_checks = 1;   			-- 외래키 체크하는 것으로 설정