CREATE DATABASE IF NOT EXISTS `sample_svc`;
USE `sample_svc`;

-- 구조
CREATE TABLE IF NOT EXISTS `t_user`(
`user_no` varchar(20) not null comment '회원번호',
`name` varchar(20) not null comment '이름',
PRIMARY KEY (`user_no`)
);

CREATE TABLE IF NOT EXISTS `t_admin`(
`user_no` varchar(20) not null DEFAULT '',
`name` varchar(20) not null COMMENT '사번',
`com_gr` varchar(20) not null COMMENT '직급',
`part_name` varchar(20) not null COMMENT '부서명',
`reg_date` date not null COMMENT '등록일자',
PRIMARY KEY (`user_no`),
CONSTRAINT `FK_t_admin_t_user` FOREIGN KEY (`user_no`) REFERENCES `t_user` (`user_no`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- 입력
INSERT INTO `t_user` (`user_no`, `name`) VALUES
('ME00001', '강민구'),
('ME00002', '이민구');

-- 구조2
CREATE TABLE IF NOT EXISTS `t_svc_use` (
`use_no` varchar(20) not null comment '서비스이용번호',
`user_no` varchar(20) not null comment '회원번호',
`use_start_dt` datetime not null comment '이용시작일시',
`use_end_dt` datetime not null comment '이용종료일시',
`use_distance` int(6) default null comment '이용거리',
`use_time` int(6) default null comment '이용시간',
`use_charge` int(6) default null comment '이용요금',
PRIMARY KEY (`use_no`),
KEY `FK_t_svc_use_t_user` (`user_no`),
CONSTRAINT `FK_t_svc_use_t_user` FOREIGN KEY (`user_no`) REFERENCES `t_user` (`user_no`) ON DELETE NO ACTION ON UPDATE NO ACTION
)

INSERT INTO `t_svc_use` (`use_no`, `user_no`, `use_start_dt`, `use_end_dt`, `use_distance`, `use_time`, `use_charge`) VALUES
('USE0001', 'ME00001', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 8 DAY), '%Y-%m-%d'), ' 12:00:00'), CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 8 DAY), '%Y-%m-%d'), ' 15:00:00'), 1200, 30, 1500),
('USE0002', 'ME00001', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 16 DAY), '%Y-%m-%d'), ' 12:00:00'), CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 16 DAY), '%Y-%m-%d'), ' 15:00:00'), 2000, 20, 3000),
('USE0003', 'ME00001', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 24 DAY), '%Y-%m-%d'), ' 12:00:00'), CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 24 DAY), '%Y-%m-%d'), ' 15:00:00'), 3200, 40, 4500),
('USE0004', 'ME00001', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 120 DAY), '%Y-%m-%d'), ' 12:00:00'), CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 120 DAY), '%Y-%m-%d'), ' 15:00:00'), 4000, 10, 6000);


-- 구조3
CREATE TABLE IF NOT EXISTS `t_svc_use_pay` (
`svc_use_pay_no` varchar(20) not null comment '서비스이용결제번호',
`use_no` varchar(20) not null comment '서비스이용번호',
`pay_datetime` datetime not null comment '결제일시',
`pay_cost` bigint(12) not null default 0 comment '결제금액',
`paymethod_code` varchar(20) not null comment '결제수단코드',
PRIMARY KEY (`svc_use_pay_no`),
KEY `FK_t_svc_use` (`use_no`),
CONSTRAINT `FK_t_svc_use` FOREIGN KEY (`use_no`) REFERENCES `t_svc_use` (`use_no`) ON DELETE NO ACTION ON UPDATE NO ACTION
)

INSERT INTO `t_svc_use_pay` (`svc_use_pay_no`, `use_no`, `pay_datetime`, `pay_cost`, `paymethod_code`) VALUES
('PAY0001', 'USE0001', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 8 DAY), '%Y-%m-%d'), ' 16:00:00'), '1500', 'C'),
('PAY0002', 'USE0002', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 16 DAY), '%Y-%m-%d'), ' 16:00:00'), '1200', 'C'),
('PAY0003', 'USE0002', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 16 DAY), '%Y-%m-%d'), ' 16:00:00'), '1800', 'P'),
('PAY0004', 'USE0003', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 24 DAY), '%Y-%m-%d'), ' 16:00:00'), '4500', 'P'),
('PAY0005', 'USE0004', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 120 DAY), '%Y-%m-%d'), ' 16:00:00'), '4000', 'C'),
('PAY0006', 'USE0004', CONCAT(DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 120 DAY), '%Y-%m-%d'), ' 16:00:00'), '2000', 'P');

