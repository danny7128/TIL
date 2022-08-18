SELECT * FROM healthcare LIMIT 1;

SELECT smoking, COUNT(*) 
FROM healthcare 
GROUP BY smoking;










SELECT age, AVG(height), AVG(weight)
FROM healthcare
GROUP BY age
HAVING AVG(height) >= 160 AND AVG(weight) >=60;






select is_drinking, count(*) from healthcare where blood_pressure >= 200 and blood_pressure != '' group by is_drinking;



SELECT is_drinking, smoking, AVG(weight / (height * 0.01 * height * 0.01)) as '평균 BMI'
FROM healthcare
GROUP BY is_drinking, smoking;



몸무게 / (키*키)

SELECT is_drinking, AVG(waist), COUNT(*)
FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;

SELECT sido, COUNT(*)
FROM healthcare
GROUP BY sido
HAVING COUNT(*) >= 50000;



SELECT height, COUNT(*)
FROM healthcare
GROUP BY height
ORDER BY COUNT(*) DESC 
LIMIT 5;

SELECT is_drinking, COUNT(*) 
FROM healthcare 
WHERE is_drinking != ''
GROUP BY is_drinking;


SELECT is_drinking, smoking, AVG(weight / (height * 0.01 * height * 0.01)) as '평균 BMI'
FROM healthcare
WHERE is_drinking != ''  AND smoking != '' 
GROUP BY is_drinking, smoking;

SELECT is_drinking, smoking, AVG(weight / (height * 0.01 * height * 0.01)) as '평균 BMI'
FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking, smoking;