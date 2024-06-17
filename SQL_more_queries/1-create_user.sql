-- creates new user user_0d_1 with all privileges

CREATE USER user_0d_1@localhost IDENTIFIED BY "user_0d_1_pwd"
GRANT ALL PRIVILEGES ON localhost TO user_0d_1@localhost;
