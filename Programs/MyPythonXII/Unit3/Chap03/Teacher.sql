create table teacher
(tno char(4) primary key not null,
tname varchar(25),
taddress varchar(30),
salary decimal(8,2) CHECK (SALARY BETWEEN 5000 AND 40000),
dept_no char(4),
doj date,
foreign key (dept_no) references department (dept_no));

insert into teacher values('T01', 'Rakesh Sharma', '245-Malviya Nagar', 25600, 'D05', '2001-12-12');
insert into teacher values('T02', 'Jugal  Mittal', '34, Ramesh Nagar', 22000, 'D02', '1999-07-03');
insert into teacher values('T03', 'Sharmila Kaur', 'D-31, Ashok Vihar', 21000, 'D01', '2000-06-06');
insert into teacher values('T04', 'Sandeep Kaushik', '	MG-32, Shalimar Bagh', 15000, 'D03', '2001-08-08');
insert into teacher values('T05', 'Sangeeta Vats', 'G-35, Malviya Nagar', 18900, 'D05', '2000-02-20');	
insert into teacher values('T06', 'Ramesh Kumar', 'BG-42, Shalimar Bagh', 24000, 'D03', '1997-07-03');
insert into teacher values('T07', 'Shyam Arora', '50, MIG FLATS, Rohini', 12000, 'D02', '1998-08-15');
insert into teacher values('T08', 'Shiv Om', 'R-44, Kirti Nagar', 13000, 'D02', '2001-09-22');
insert into teacher values('T09', 'Vivek Rawat', 'E-33/27, Sec-1, Rohini', 17000, 'D01', '2001-10-12');
insert into teacher values('T10', 'Rajest Verma', 'D-11/130, Sec-5, Dwaraka', 15600, 'D04', '2000-11-07');
insert into teacher values('T11', 'Ashok Singhal', 'F-1/65, East Patel Ngr', 17500, 'D02', '1999-08-11');
insert into teacher values('T12', 'Chetan Shukla', 'C-105, Vikash Pur', 13400, 'D02', '2001-06-13');
insert into teacher values('T13', 'Reena Mehta', '120, DDA Colony, Rohini', 15500, 'D03', '2000-07-18');
insert into teacher values('T14', 'Bhwana Lamba', 'E-140, Swastik Apptt., DLF', 14500, 'D04', '2001-07-16');
insert into teacher values('T15', 'Jagjit Singh', 'A-24D, Printers Apptt., Rohini', 16500, 'D04', '1889-07-11');
INSERT INTO TEACHER (TNO , TNAME , TADDRESS, DEPT_NO, DOJ) VALUES('T16', 'Dinesh Goel', 'A-21, Sec-12, Dwarka', 'D04', '2000-Oct-12');
INSERT INTO TEACHER (TNO , TNAME , TADDRESS, DEPT_NO, DOJ) VALUES('T17', 'Lokesh Rathore', 'PU-120, Pitam Pura', 'D03', '1999-Jul-17');
INSERT INTO TEACHER VALUES('T18', 'Akash Rathi', 'A-52, Sansad Marg', 15700, 'D03', '2000-07-18');
INSERT INTO TEACHER VALUES('T19', 'Simran Chawla', 'D-1/120, Sec-5, Rohini', 14700, 'D04', '2001-07-16');