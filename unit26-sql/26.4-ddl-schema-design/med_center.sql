DROP DATABASE IF EXISTS medical_center;

CREATE DATABASE medical_center;

\c medical_center;

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
);

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
);

CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15)
);

CREATE TABLE visit_log (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    intake_resaon VARCHAR(30),
    intake_date DATETIME NOT NULL
);

CREATE TABLE diagnosis_log (
    id SERIAL PRIMARY KEY,
    visit_id INTEGER REFERENCES visit_log,
    diagnosis INTEGER REFERENCES diseases,
    doctor_id INTEGER REFERENCES doctors,
);

CREATE TABLE current_patients (
    patient_id INTEGER REFERENCES patients,
    doctor_id INTEGER REFERENCES doctors,
    intake_id INTEGER REFERENCES visit_log
);
