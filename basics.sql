-- creating a table
CREATE TABLE example_table (
    column1 INT,
    column2 VARCHAR(50),
    column3 DATE
);

-- Insert some data into the table (optional)
INSERT INTO example_table (column1, column2, column3)
VALUES (1, 'Data 1', '2024-05-11'),
      (2, 'Data 2', '2024-05-12'),
      (3, 'Data 3', '2024-05-13');

-- showing the table contents
SELECT * FROM example_table;

-- deleting a column from a table
ALTER TABLE table_name
DROP COLUMN column_name;

-- Adding a column to a table
ALTER TABLE table_name
ADD column_name data_type --[constraints];

-- adding a column after a specific existing column
ALTER TABLE existing_table
ADD new_column INT AFTER existing_column;

-- deleting a specific row from an existing table
DELETE FROM table_name
WHERE condition;
-- Example
DELETE FROM employees
WHERE employee_id = 123;

-- delete all rows from a table
DELETE FROM table_name

-- deleting a table
DROP TABLE table_name

-- modifying columns values
UPDATE table_name
SET column1 = new_value1, column2 = new_value2, ...
WHERE condition;
-- Example
UPDATE employees
SET department = 'Finance'
WHERE employee_id = 1;

-- showing content of table in a specific order 
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC | DESC], column2 [ASC | DESC], ...;
-- Example 
SELECT employee_id, first_name, last_name, salary
FROM employees
ORDER BY salary DESC;















