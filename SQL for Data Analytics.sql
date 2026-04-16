
--  MODULE 4 — DA: SQL — Introduction and Getting Started with SQL

DROP DATABASE IF EXISTS da_module4;
CREATE DATABASE da_module4;

USE da_module4;

DROP TABLE IF EXISTS Worker;

CREATE TABLE Worker (WORKER_ID    INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
					 FIRST_NAME   VARCHAR(25)    NOT NULL,
                     LAST_NAME    VARCHAR(25)    NOT NULL,
                     SALARY       DECIMAL(12,2)  NOT NULL,
                     JOINING_DATE DATETIME       NOT NULL,
                     DEPARTMENT   VARCHAR(25)    NOT NULL);

INSERT INTO Worker
    (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT)
VALUES
    (1,  'Monika',  'Arora',   100000.00, '2014-02-20 09:00:00', 'HR'),
    (2,  'Niharika','Verma',    80000.00, '2014-06-11 09:00:00', 'Admin'),
    (3,  'Vishal',  'Singhal', 300000.00, '2014-02-20 09:00:00', 'HR'),
    (4,  'Amitabh', 'Singh',   500000.00, '2014-02-20 09:00:00', 'Admin'),
    (5,  'Vivek',   'Bhati',   500000.00, '2014-06-11 09:00:00', 'Admin'),
    (6,  'Vipul',   'Diwan',   200000.00, '2014-06-11 09:00:00', 'Account'),
    (7,  'Satish',  'Kumar',    75000.00, '2014-01-20 09:00:00', 'Account'),
    (8,  'Geetika', 'Chauhan',  90000.00, '2014-04-11 09:00:00', 'Admin');

SELECT * FROM Worker;

-- Q1. Print all Worker details ordered by FIRST_NAME Ascending and DEPARTMENT Descending.
SELECT
    WORKER_ID,
    FIRST_NAME,
    LAST_NAME,
    SALARY,
    JOINING_DATE,
    DEPARTMENT
FROM Worker
ORDER BY
    FIRST_NAME  ASC,
    DEPARTMENT  DESC;
    
-- Q2. Print details for Workers with FIRST_NAME "Vipul" and "Satish".
SELECT * FROM Worker
WHERE FIRST_NAME IN ('Vipul', 'Satish');

-- Q3. Print details of Workers whose FIRST_NAME ends with 'h'
--     and contains exactly six alphabets.
SELECT *
FROM Worker
WHERE FIRST_NAME LIKE '_____h';

-- Q4. Print details of Workers whose SALARY lies between
--     100,000 and 500,000 (inclusive).
SELECT *
FROM Worker
WHERE SALARY BETWEEN 100000 AND 500000
ORDER BY SALARY;

-- Q5. Fetch duplicate records having matching data in some fields.
--     Method A: Find duplicate FIRST_NAME + DEPARTMENT combinations.
SELECT
    FIRST_NAME,
    DEPARTMENT,
    COUNT(*) AS DuplicateCount
FROM Worker
GROUP BY FIRST_NAME, DEPARTMENT
HAVING COUNT(*) > 1;

-- Q6. Show the top 6 records of the Worker table.
SELECT *
FROM Worker
ORDER BY WORKER_ID
LIMIT 6;

-- Q7. Fetch departments that have fewer than 5 people in them.
SELECT
    DEPARTMENT,
    COUNT(*) AS Employee_Count
FROM Worker
GROUP BY DEPARTMENT
HAVING COUNT(*) < 5
ORDER BY Employee_Count DESC;

-- Q8. Show all departments along with the number of people in each.
SELECT
    DEPARTMENT,
    COUNT(*)          AS Total_Employees,
    SUM(SALARY)       AS Total_Salary,
    AVG(SALARY)       AS Avg_Salary,
    MAX(SALARY)       AS Max_Salary,
    MIN(SALARY)       AS Min_Salary
FROM Worker
GROUP BY DEPARTMENT
ORDER BY Total_Employees DESC;

-- Q9. Print the name of employees having the HIGHEST SALARY
--     in each department.
SELECT
    w.FIRST_NAME,
    w.LAST_NAME,
    w.DEPARTMENT,
    w.SALARY
FROM Worker w
WHERE w.SALARY = (
    SELECT MAX(w2.SALARY)
    FROM   Worker w2
    WHERE  w2.DEPARTMENT = w.DEPARTMENT
)
ORDER BY w.DEPARTMENT;



--  ASSESSMENT 2 — Student Table

DROP TABLE IF EXISTS student;

CREATE TABLE student (
    StdID      INT          NOT NULL PRIMARY KEY,
    StdName    VARCHAR(50)  NOT NULL,
    Sex        ENUM('Male','Female') NOT NULL,
    Percentage DECIMAL(5,2) NOT NULL,
    Class      INT          NOT NULL,
    Sec        CHAR(1)      NOT NULL,
    Stream     VARCHAR(20)  NOT NULL,
    DOB        DATE         NOT NULL
);
INSERT INTO student
    (StdID, StdName, Sex, Percentage, Class, Sec, Stream, DOB)
VALUES
    (1001, 'Surekha Joshi',   'Female', 82.00, 12, 'A', 'Science',  '1998-03-08'),
    (1002, 'MAAHI AGARWAL',   'Female', 56.00, 11, 'C', 'Commerce', '2008-11-23'),
    (1003, 'Sanam Verma',     'Male',   59.00, 11, 'C', 'Commerce', '2006-06-29'),
    (1004, 'Ronit Kumar',     'Male',   63.00, 11, 'C', 'Commerce', '1997-11-05'),
    (1005, 'Dipesh Pulkit',   'Male',   78.00, 11, 'B', 'Science',  '2003-09-14'),
    (1006, 'JAHANVI Puri',    'Female', 60.00, 11, 'B', 'Commerce', '2008-11-07'),
    (1007, 'Sanam Kumar',     'Male',   23.00, 12, 'F', 'Commerce', '1998-03-08'),
    (1008, 'SAHIL SARAS',     'Male',   56.00, 11, 'C', 'Commerce', '2008-11-07'),
    (1009, 'AKSHRA AGARWAL',  'Female', 72.00, 11, 'B', 'Commerce', '1996-10-01'),
    (1010, 'STUTI MISHRA',    'Female', 39.00, 11, 'F', 'Science',  '2008-11-23'),
    (1011, 'HARSH AGARWAL',   'Male',   42.00, 11, 'C', 'Science',  '1998-03-08'),
    (1012, 'NIKUNJ AGARWAL',  'Male',   49.00, 12, 'C', 'Commerce', '1998-06-28'),
    (1013, 'AKRITI SAXENA',   'Female', 89.00, 12, 'A', 'Science',  '2008-11-23'),
    (1014, 'TANI RASTOGI',    'Female', 82.00, 12, 'A', 'Science',  '2008-11-23');
    
SELECT * FROM student;

-- Q1. Display ALL records from STUDENT table.
SELECT * FROM student;

-- Q2. Display student name and date of birth from STUDENT table.
SELECT StdName, DOB FROM student;

-- Q3. Display all students where percentage >= 80.
SELECT * FROM student WHERE Percentage >= 80;

-- Q4. Display student name, stream and percentage where
--     percentage > 80.
SELECT StdName, Stream, Percentage
FROM   student
WHERE  Percentage > 80;

-- Q5. Display all records of Science students whose
--     percentage > 75.
SELECT *
FROM   student
WHERE  Stream = 'Science'
AND    Percentage > 75;



