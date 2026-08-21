
-- Task 1
-- Select the database 'internnova'   
use internnova;

-- Create a 'Students' table 
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Course VARCHAR(50),
    Grade VARCHAR(5)
);

--  Add few records in the 'Students' table
INSERT INTO Students (StudentID, Name, Age, Course, Grade)
VALUES
(101, 'Vishal', 20, 'Computer Science', 'A'),
(102, 'Seeya', 21, 'Information Tech', 'B+'),
(103, 'Ankita', 19, 'Business Studies', 'A-'),
(104, 'Sunny', 22, 'Software Engineering', 'B');

-- SQL queries to display all records.
SELECT * FROM students; 

-- Select specific columns using SELECT.
SELECT name, age, course FROM students;

-- Use column aliases where appropriate. 
SELECT studentid as Roll_No, name AS Student_Name, age AS Age, course AS Course FROM students;
