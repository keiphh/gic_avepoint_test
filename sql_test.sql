-- Qn 1
SELECT 
	employeeid, 
	salary, 
	CASE
        WHEN salary < 5000 THEN 'less than 5000'
        WHEN salary BETWEEN 5000 AND 10000 THEN 'between 5000 and 10000'
        WHEN salary > 10000 THEN 'more than 10000'
    END AS salary_band 
FROM employee

-- Qn 2 
SELECT 
	department, 
	MAX(salary) AS highest_salary, 
	MIN(salary) AS lowest_salary, 
	AVG(salary) AS average_salary 
FROM employee
GROUP BY department
HAVING COUNT(employeeid) < 3

-- Qn 3
SELECT 
    department,
    COUNT(DISTINCT salary) AS unique_salary_count
FROM employee
GROUP BY department;

-- Qn 4
SELECT 
    e1.department,
    e1.employeeid
FROM employee e1
JOIN employee e2 ON e1.department = e2.department 
    AND e1.salary = e2.salary
    AND e1.employeeid <> e2.employeeid

-- Qn 5
WITH RankedSalaries AS (
    SELECT 
        department,
        salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employee
)
SELECT DISTINCT 
	department,
    salary
FROM RankedSalaries
WHERE rank <= 3
ORDER BY department, salary DESC