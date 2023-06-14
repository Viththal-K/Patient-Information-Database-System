-- Creates the database
CREATE DATABASE patient_db;

-- Switches to the database
USE patient_db;

-- Creates the patient_info table
CREATE TABLE patient_info (
    name VARCHAR(40),
    reference VARCHAR(40),
    age VARCHAR(40),
    gender VARCHAR(40),
    illness VARCHAR(40),
    medication VARCHAR(40),
    date VARCHAR(40)
);

-- To view records in the table
SELECT * from patient_info;
