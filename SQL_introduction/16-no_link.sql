-- retrieves all rows with names in second_table
-- rows are listed by score in descending order

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
