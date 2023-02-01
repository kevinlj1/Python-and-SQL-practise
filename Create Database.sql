CREATE DATABASE IF NOT EXISTS testScores;

USE testScores;

CREATE TABLE IF NOT EXISTS users (

usersID int NOT NULL AUTO_INCREMENT,
UserName varchar(30),
ICTScore int,
MathsScore int,
ChemistryScore int,

PRIMARY KEY (usersID)
);


/* SELECT * FROM users; */