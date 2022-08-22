SELECT * 
FROM playlist_track AS A
ORDER BY A.PlaylistId DESC
LIMIT 5;


SELECT *
FROM tracks AS B
ORDER BY TrackId ASC
LIMIT 5;


SELECT *
FROM playlist_track
LIMIT 5 ;

SELECT *
FROM tracks
LIMIT 5 ;

SELECT PlaylistId, Name
FROM playlist_track INNER JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
    ORDER BY PlaylistId DESC
    LIMIT 10;

SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 10;




SELECT *
FROM playlist_track A
LIMIT 1;

SELECT *
FROM tracks B
LIMIT 1;

SELECT A.PlaylistId, B.Name
FROM playlist_track A INNER JOIN tracks B
    ON A.TrackId = B.TrackId
    WHERE A.PlaylistId = 10
    ORDER BY B.Name DESC
    LIMIT 5;

SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC
LIMIT 5;


SELECT *
FROM tracks
LIMIT 10;

SELECT *
FROM artists
LIMIT 10;

SELECT COUNT(*)
FROM tracks A INNER JOIN artists B
    ON A.Composer = B.Name;

SELECT COUNT(*)
FROM tracks A LEFT JOIN artists B
    ON A.Composer = B.Name;

SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;

SELECT InvoiceLineId, InvoiceId FROM invoice_items
ORDER BY InvoiceId 
LIMIT 5;


SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;

SELECT A.InvoiceLineId, B.InvoiceId
FROM invoice_items A INNER JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
ORDER BY A.InvoiceId ASC
LIMIT 5;


SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC
LIMIT 5;



SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC
LIMIT 5;

SELECT A.InvoiceId, B.CustomerId FROM invoices A
INNER JOIN customers B
ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;



SELECT A.InvoiceId, B.CustomerId
FROM invoices A INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
ORDER BY InvoiceId DESC
LIMIT 5;


SELECT A.InvoiceLineId, A.InvoiceId, C.CustomerId 
FROM invoice_items A
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;


SELECT A.InvoiceLineId, B.InvoiceId, B.CustomerId
FROM invoice_items A 
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;




SELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;





SELECT A.InvoiceLineId, B.InvoiceId, B.CustomerId
FROM invoice_items A 
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;



SELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;

SELECT C.CustomerId, COUNT(*)
FROM invoice_items A 
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;

