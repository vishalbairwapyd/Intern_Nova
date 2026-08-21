-- select database 
USE company_db;
/* inner join
-- Display employees along with their department names*/
SELECT
    e.EmployeeID,
    e.EmployeeName,
    e.Salary,
    d.DepartmentName
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID;