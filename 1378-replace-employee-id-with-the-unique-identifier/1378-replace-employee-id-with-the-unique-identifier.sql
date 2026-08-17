# Write your MySQL query statement below
SELECT U.unique_id, E.name
FROM Employees as E
LEFT JOIN EmployeeUNI as U on E.id = U.id