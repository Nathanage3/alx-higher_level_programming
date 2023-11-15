-- Create db hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Grant user_0d_02
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant the select privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;
