Creating a New MySQL User:

CREATE USER 'username'@'host' IDENTIFIED BY 'password';
This command creates a new user within MySQL with specified login credentials.
Managing Privileges:

GRANT ALL PRIVILEGES ON database.table TO 'username'@'host';
This command assigns privileges to a user for specific databases or tables.
PRIMARY KEY:

A PRIMARY KEY is a unique identifier for a record in a table and ensures that the column or set of columns defined as the primary key contains no duplicate values.
FOREIGN KEY:

A FOREIGN KEY is a field (or collection of fields) in one table that uniquely identifies a row of another table. It is used to establish and enforce a link between the data in two tables.
NOT NULL and UNIQUE Constraints:

The NOT NULL constraint ensures that a column cannot have a NULL value.
The UNIQUE constraint ensures that all values in a column are different.
Retrieving Data from Multiple Tables:

You can retrieve data from multiple tables in one SQL query using JOIN clauses:
SELECT * FROM table1 INNER JOIN table2 ON table1.common_field = table2.common_field;
Subqueries:

A subquery is a query nested within another query and can be used to perform operations that would be complex in a single query.
JOIN and UNION:

JOIN is used to combine rows from two or more tables based on a related column between them.
UNION is used to combine the results of two or more SELECT statements into a single result set.

Illustrative examples


Creating a New MySQL User:
sql
Copy code
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
Managing Privileges:
sql
Copy code
-- Grant SELECT privilege on all tables in mydb to the user.
GRANT SELECT ON mydb.* TO 'newuser'@'localhost';

-- Grant ALL privileges on the 'users' table in mydb to the user.
GRANT ALL PRIVILEGES ON mydb.users TO 'newuser'@'localhost';
PRIMARY KEY:
sql

-- Creating a table with a PRIMARY KEY
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    student_name VARCHAR(100),
    PRIMARY KEY (student_id)
);
FOREIGN KEY:
sql

-- Creating a table with a FOREIGN KEY
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
NOT NULL and UNIQUE Constraints:
sql

-- Creating a table with NOT NULL and UNIQUE constraints
CREATE TABLE users (
    user_id INT AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (user_id)
);
Retrieving Data from Multiple Tables:
sql

-- Using an INNER JOIN to retrieve data from multiple tables
SELECT students.student_name, enrollments.course_id
FROM students
INNER JOIN enrollments ON students.student_id = enrollments.student_id;
Subqueries:
sql

-- Using a subquery to select users who have made more than one order
SELECT username
FROM users
WHERE user_id IN (SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) > 1);
JOIN and UNION:
sql

-- Using a JOIN to combine rows from two tables
SELECT employees.name, departments.name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;

-- Using a UNION to combine the results of two SELECT statements
SELECT student_name FROM undergraduate_students
UNION
SELECT student_name FROM graduate_students;
