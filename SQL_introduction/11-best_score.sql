-- retrieves rows for second_table with scores 10+
-- rows are listed by score in descending order

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
