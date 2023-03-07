--
-- SQLINES DEMO *** or table `admin`
--

DROP TABLE IF EXISTS admin;

CREATE SEQUENCE admin_seq;

CREATE TABLE admin (
  id int NOT NULL DEFAULT NEXTVAL ('admin_seq'),
  name varchar(45) DEFAULT NULL,
  password varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
)   ;

ALTER SEQUENCE admin_seq RESTART WITH 2;

INSERT INTO admin VALUES (1,'admin','123456');

select * from admin
--
-- SQLINES DEMO *** or table `department`
--

DROP TABLE IF EXISTS department;

CREATE SEQUENCE department_seq;

CREATE TABLE department (
  id int NOT NULL DEFAULT NEXTVAL ('department_seq'),
  name varchar(45) DEFAULT NULL,
  registration_fee decimal(10,2) DEFAULT NULL,
  doctor_num int DEFAULT '0',
  PRIMARY KEY (id)
)   ;

ALTER SEQUENCE department_seq RESTART WITH 9;

INSERT INTO department VALUES (1,'Paediatrics',20.00,0),(2,'Gynaecology',20.00,0),(3,'Medicine',20.00,0),(4,'Surgery',20.00,0),(5,'Opthamology',20.00,0),(6,'Orthopedics',25.00,0),(7,'Dermatology',25.00,0),(8,'Otorhinolaryngology',20.00,0);



--
-- SQLINES DEMO *** or table `medicine`
--

DROP TABLE IF EXISTS medicine;

CREATE SEQUENCE medicine_seq;

CREATE TABLE medicine (
  id int NOT NULL DEFAULT NEXTVAL ('medicine_seq'),
  name varchar(45) DEFAULT NULL,
  price varchar(45) DEFAULT NULL,
  unit varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
)   ;

ALTER SEQUENCE medicine_seq RESTART WITH 5;

INSERT INTO medicine VALUES (1,'lisinopril','15','Boxes'),(2,'Vitamin C','20','Bottles'),(3,'Metformin','12','Bottles'),(4,'Panadol','20','Boxes');


--
-- SQLINES DEMO *** or table `order`
--

DROP TABLE IF EXISTS orderr;

CREATE SEQUENCE order_seq;

CREATE TABLE orderr (
  id int NOT NULL DEFAULT NEXTVAL ('order_seq'),
  patient_id int DEFAULT NULL,
  department_id int DEFAULT NULL,
  readme varchar(200) DEFAULT NULL ,
  registration_fee decimal(10,2) DEFAULT NULL ,
  doctor_id int DEFAULT NULL ,
  order_advice varchar(400) DEFAULT NULL ,
  medicine_list varchar(45) DEFAULT NULL ,
  total_cost decimal(10,2) DEFAULT NULL,
  status int DEFAULT NULL,
  time timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
)   ;

ALTER SEQUENCE order_seq RESTART WITH 5;

INSERT INTO orderr VALUES (1,1,1,'Insomnia',20.00,1,'Medication','2',40.00,2,'2021-09-07 00:00:00'),(2,1,7,'Patellofemoral pain',NULL,NULL,'',NULL,NULL,1,'2021-09-13 18:58:13'),(3,2,1,'Headache',20.00,1,'Light Flu, More rest','1,2',55.00,2,'2021-09-14 15:26:54'),(4,3,1,'Dizzy',20.00,1,'Heat stroke, More rest','1,2',55.00,2,'2021-09-14 16:22:18');



--
-- SQLINES DEMO *** or table `user_doctor`
--

DROP TABLE IF EXISTS user_doctor;

CREATE SEQUENCE user_doctor_seq;

CREATE TABLE user_doctor (
  id int NOT NULL DEFAULT NEXTVAL ('user_doctor_seq'),
  name varchar(45) DEFAULT NULL ,
  id_card varchar(45) DEFAULT NULL ,
  department_id int DEFAULT NULL ,
  status int DEFAULT NULL ,
  password varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
)  ;


ALTER SEQUENCE user_doctor_seq RESTART WITH 5;

INSERT INTO user_doctor VALUES (1,'Doctor Lim','310116199001011234',1,1,'123456'),(2,'Doctor Jane','310116199001021234',2,1,'123456'),(3,'Doctor Alice','310116199001031234',3,1,'123456'),(4,'Doctor Alex','310116199001041234',4,1,'123456');


--
-- SQLINES DEMO *** or table `user_patient`: Doctor inputs new medication requests
--

DROP TABLE IF EXISTS user_patient;

CREATE SEQUENCE slot_sequence
INCREMENT 1
MINVALUE 1
MAXVALUE 6
START 1
CYCLE;

CREATE SEQUENCE id_seq;
CREATE SEQUENCE job_seq;
CREATE SEQUENCE order_seq;

CREATE TABLE user_patient (
	id int NOT NULL DEFAULT NEXTVAL ('id_seq') PRIMARY KEY,
	job_id TEXT NOT NULL DEFAULT 'P-'||nextval('job_seq'::regclass)::TEXT, 
	order_id TEXT NOT NULL DEFAULT 'EMR-'||nextval('order_seq'::regclass)::TEXT, 
  	box_number INT DEFAULT 0,
  	ward_number int DEFAULT NULL ,
  	status VARCHAR(64),
	recorded_date varchar(45),
	recorded_time varchar(45),
	slot_number varchar(45) DEFAULT NEXTVAL ('slot_sequence')
)   ;

ALTER SEQUENCE slot_sequence RESTART WITH 5;
ALTER SEQUENCE id_seq RESTART WITH 5;

/*Note: Without defining a Primary Key, Django assumes a primary key column named id. 
However this column doesn't actually exist in the table. Therefore I get the error "column test.id does not exist"*/


INSERT INTO user_patient VALUES 
(1, 'P-1274', 'EMR-1839', '9', '1', 'PickedUp', '2021-09-07', '00:00:00', '1'), 
(2, 'P-1129', 'EMR-2842', '1','5', 'DroppedOff', '2021-09-13', '18:58:13', '2'), 
(3, 'P-2748', 'EMR-9471', '2', '2', 'Completed', '2021-09-13', '18:58:13', '3'), 
(4, 'P-182', 'EMR-0193', '8', '3', 'Pending', '2021-09-14', '16:22:18', '4')

select * from user_patient


/********** Nurses: QR Output **********/
DROP TABLE IF EXISTS nurse_QR;

CREATE SEQUENCE QR_id;

CREATE TABLE nurse_QR (
	id int NOT NULL DEFAULT NEXTVAL ('QR_id') PRIMARY KEY,
  	output VARCHAR(64)
)   ;

ALTER SEQUENCE QR_id RESTART WITH 2;

insert into nurse_QR (id, output) values (1, '1235850693');

select * from nurse_QR


/********** Date selected for past records **********/
DROP TABLE IF EXISTS test_date;

CREATE SEQUENCE id_test;

CREATE TABLE test_date (
	id int NOT NULL DEFAULT NEXTVAL ('id_test') PRIMARY KEY,
  	select_date varchar(45) DEFAULT NULL
)   ;

ALTER SEQUENCE id_test RESTART WITH 4;

insert into test_date (id, select_date) values (1, '2023-01-05');
insert into test_date (id, select_date) values (2, '2023-01-15');
insert into test_date (id, select_date) values (3, '2023-01-17');

select * from test_date


-- EMR Database --

DROP TABLE IF EXISTS patients_data;

CREATE SEQUENCE CPS_seq;

CREATE SEQUENCE order_seq;

CREATE TABLE patients_data(
	id int NOT NULL DEFAULT NEXTVAL ('CPS_seq') PRIMARY KEY,
	order_id TEXT NOT NULL DEFAULT 'EMR-'||nextval('test_seq'::regclass)::TEXT,
	ward_number INT
);

ALTER SEQUENCE CPS_seq RESTART WITH 5;

insert into patients_data (id, order_id, ward_number) values (1, 'EMR-133', 5);
insert into patients_data (id, order_id, ward_number) values (2, 'EMR-9378', 1);
insert into patients_data (id, order_id, ward_number) values (3, 'EMR-2480', 4);
insert into patients_data (id, order_id, ward_number) values (4, 'EMR-144', 1);

SELECT * FROM patients_data














