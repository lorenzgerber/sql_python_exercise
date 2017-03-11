

/*Retrieves person info and the total amount of know hours worked by each employee*/
SELECT SSN, LName, FName, MInit, COALESCE(SUM(Hour),0) AS Know_Hours
FROM Employee LEFT OUTER JOIN Works_On ON (SSN=ESSN)
GROUP BY SSN;

/*Counts how many projects an employee works on which has no record of worked hours, used for Unknown_Hours and Overtime*/
SELECT ESSN, COUNT(PNo)
FROM Works_On
WHERE (NOT (ESSN IN(SELECT ESSN 
					FROM Works_On
					WHERE Hours IS NOT NULL)))
GROUP BY ESSN, PNo;