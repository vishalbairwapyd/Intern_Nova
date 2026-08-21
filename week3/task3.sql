-- Task 3 
-- Ready a setup to perform all the subtasks in Task3
-- Create a 'company_db' database
CREATE DATABASE company_db;

-- Select 'company_db' database 
USE company_db;

-- Create 'Departments' Table and insert data inside it
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50),
    Location VARCHAR(50)
);

INSERT INTO Departments (DepartmentID, DepartmentName, Location)
VALUES
(1, 'IT', 'Delhi'),
(2, 'HR', 'Gurgaon'),
(3, 'Finance', 'Mumbai'),
(4, 'Sales', 'Chandigarh'),
(5, 'Marketing', 'Jaipur'),
(6, 'Operations', 'Pune');

-- Create 'Employees' Table and insert data inside it
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    DepartmentID INT,
    Salary DECIMAL(10,2),
    JoiningDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Employees
(EmployeeID, EmployeeName, Age, Gender, DepartmentID, Salary, JoiningDate)
VALUES
(101, 'Amit Sharma', 25, 'Male', 1, 55000, '2022-01-15'),
(102, 'Priya Singh', 28, 'Female', 1, 72000, '2021-03-20'),
(103, 'Rahul Verma', 30, 'Male', 1, 85000, '2020-07-10'),
(104, 'Neha Gupta', 26, 'Female', 2, 48000, '2023-02-12'),
(105, 'Rohit Kumar', 32, 'Male', 2, 62000, '2019-11-05'),
(106, 'Sneha Mehta', 29, 'Female', 2, 58000, '2021-08-18'),
(107, 'Vikas Yadav', 35, 'Male', 3, 90000, '2018-06-25'),
(108, 'Anjali Rao', 27, 'Female', 3, 68000, '2022-09-14'),
(109, 'Manish Jain', 31, 'Male', 3, 75000, '2020-04-16'),
(110, 'Pooja Saini', 24, 'Female', 4, 42000, '2023-05-22'),
(111, 'Suresh Patel', 38, 'Male', 4, 65000, '2017-10-11'),
(112, 'Kavita Joshi', 29, 'Female', 4, 58000, '2021-12-01'),
(113, 'Arjun Malhotra', 27, 'Male', 5, 60000, '2022-04-19'),
(114, 'Riya Kapoor', 25, 'Female', 5, 52000, '2023-01-10'),
(115, 'Deepak Sharma', 34, 'Male', 5, 70000, '2019-08-30'),
(116, 'Nitin Arora', 33, 'Male', 6, 58000, '2020-02-15'),
(117, 'Simran Kaur', 28, 'Female', 6, 64000, '2021-06-20'),
(118, 'Gaurav Bansal', 36, 'Male', 6, 78000, '2018-12-05');

/* Group records using GROUP BY
Count no. of employees in each department */ 
SELECT
    d.DepartmentName,
    COUNT(e.EmployeeID) AS Total_Employees
FROM Departments d
JOIN Employees e
    ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentName;

-- Calculate aggregate values for each group.
SELECT
    d.DepartmentName,
    COUNT(e.EmployeeID) AS Total_Employees,
    SUM(e.Salary) AS Total_Salary,
    AVG(e.Salary) AS Average_Salary,
    MIN(e.Salary) AS Minimum_Salary,
    MAX(e.Salary) AS Maximum_Salary
FROM Departments d
JOIN Employees e
    ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentName;

/* Use the HAVING clause to filter grouped results.
Find the average salary in each department */
SELECT
    DepartmentID,
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY DepartmentID
HAVING AVG(Salary) > 60000;