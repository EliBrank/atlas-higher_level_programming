-- retrieves number of instances for each score in second_table

SELECT score, COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
