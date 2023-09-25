CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    MRN VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE demographics (
    demographic_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    address TEXT,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
