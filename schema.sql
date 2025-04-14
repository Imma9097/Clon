-- Database: clon_point_credit

-- Create the database
CREATE DATABASE IF NOT EXISTS clon_point_credit;

-- Use the database
USE clon_point_credit;

-- Table: clients
CREATE TABLE IF NOT EXISTS clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    id_number VARCHAR(20) NOT NULL UNIQUE,
    mobile_number VARCHAR(15) NOT NULL,
    residence VARCHAR(100) NOT NULL,
    business_type VARCHAR(50) NOT NULL,
    business_location VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: loans
CREATE TABLE IF NOT EXISTS loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    principal_amount FLOAT NOT NULL,
    interest_rate FLOAT DEFAULT 8.0, -- 8% per week
    appraisal_fee FLOAT DEFAULT 300.0,
    weekly_installment FLOAT NOT NULL,
    penalty_rate FLOAT DEFAULT 10.0, -- 10% penalty
    status ENUM('Active', 'Cleared', 'Defaulted') DEFAULT 'Active',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Table: payments
CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT NOT NULL,
    amount_paid FLOAT NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_type ENUM('Interest', 'Principal', 'Installment') NOT NULL,
    balance_remaining FLOAT NOT NULL,
    FOREIGN KEY (loan_id) REFERENCES loans(id) ON DELETE CASCADE
);

-- Table: reports
CREATE TABLE IF NOT EXISTS reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_type ENUM('Daily', 'Weekly', 'Monthly', 'Graphical') NOT NULL,
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    report_data TEXT -- Stores JSON or text data for the report
);