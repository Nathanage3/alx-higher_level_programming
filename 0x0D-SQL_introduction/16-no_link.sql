-- list all records on the table second_list excluding rows without name
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
