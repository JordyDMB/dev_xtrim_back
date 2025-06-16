CREATE DATABASE IF NOT EXISTS database_dev;
USE database_dev;

CREATE TABLE IF NOT EXISTS consumption (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    consumption_type VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    consumption_date DATE NOT NULL,
    consumption_time TIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos de ejemplo
INSERT INTO consumption (user_id, consumption_type, amount, consumption_date, consumption_time)
VALUES 
(1, 'mg', 1000.50, '2025-06-01', '10:00:00'),
(1, 'mg', 1450.75, '2025-06-05', '09:30:00'),
(1, 'mg', 2000.00, '2025-06-03', '14:15:00');
