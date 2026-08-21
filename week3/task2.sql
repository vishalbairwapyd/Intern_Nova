
-- select 'Students' database
USE internnova;

/*Filter records using the WHERE clause
   Students older than 20*/
SELECT * FROM Students WHERE Age > 20;

/* Use comparison operators in conditions.
 Fetch only 'computer science' students records */
SELECT * FROM Students WHERE Course = 'Computer Science';

/* Sort records using ORDER BY 
Display 'Students' table records in latest order
*/
SELECT * FROM Students ORDER BY studentid desc;

-- Perform calculations using aggregate functions: 
SELECT COUNT(*) as Total_Students,
SUM(age) AS Sum_of_ages, AVG(age) AS Average_age,
MIN(age) AS Minimum_age, MAX(age) AS Maximum_age 
FROM students;


