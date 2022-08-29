SELECT * FROM invoices LIMIT 1;





SELECT ArtistId, COUNT(*) AS '앨범 수'
FROM albums 
GROUP BY ArtistId
HAVING COUNT(*) >= 10
ORDER BY COUNT(*) DESC;



SELECT COUNT(*) AS "고객 수", Country, State
FROM customers
WHERE State NOTNULL
GROUP BY Country, State
ORDER BY "고객 수" DESC, Country DESC
LIMIT 5;


SELECT CASE 
FROM 


SELECT CustomerId, 
  CASE
    WHEN Fax ISNULL THEN 'X'
    WHEN Fax NOTNULL THEN 'O'
    END AS 'Fax 유/무'
FROM customers
ORDER BY CustomerId
LIMIT 5;


SELECT ArtistId, COUNT(*)
FROM artists
GROUP BY ArtistId;

SELECT *
FROM artists
LIMIT 1;


SELECT *
FROM albums
LIMIT 1;

SELECT ArtistId, COUNT(*), (SELECT Name FROM artists) AS 'Name'
FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC
LIMIT 1;



SELECT * 
FROM artists
LIMIT 1;

SELECT * 
FROM albums
LIMIT 1;

SELECT ArtistId, COUNT(*), (SELECT Name FROM artists) AS 'Name'
FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC
LIMIT 1;





SELECT COUNT(*)
FROM invoices
WHERE strftime('%Y', InvoiceDate) = '2013';



SELECT *
FROM invoices
LIMIT 1;



SELECT LastName, FirstName, strftime("%Y", "NOW") - strftime("%Y", BirthDate) + 1 as '나이'
FROM employees
ORDER BY EmployeeId;