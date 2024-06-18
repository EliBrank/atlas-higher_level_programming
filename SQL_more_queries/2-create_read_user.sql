-- create database hbtn_0d_2 and user user_0d_2 with SELECT privilege on database

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON *.* TO user_0d_2@localhost;
