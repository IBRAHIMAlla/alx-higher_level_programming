-- computes the score average of all records in the table second_table of the database hbtn_0c_0
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
