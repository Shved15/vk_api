CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(33),
    last_name VARCHAR(33),
    age INT
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE clients_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    order_id INT,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

INSERT INTO clients (first_name, last_name, age) VALUES
('Petr', 'Kurkov', 31),
('Katerina', 'Petrova', 67),
('Petr', 'Ivanov', 22),
('Max', 'Zvonov', 35),
('Ira', 'Artemova', 16);

INSERT INTO orders (product, category) VALUES
('Samsung S21', 'Mobile'),
('Dell 15” 1Tb 3.6Gz 32 RAM', 'PC'),
('Iphone 12', 'Mobile'),
('MacBook Air', 'PC'),
('Battery AAA', 'Accessory');

INSERT INTO clients_orders (client_id, order_id) VALUES
(1, 1),
(2, 1),
(1, 3),
(2, 3),
(3, 1),
(3, 2),
(3, 5),
(4, 3),
(5, 4);

SELECT clients.first_name, clients.last_name, clients.age
FROM clients
JOIN clients_orders ON clients.id = clients_orders.client_id
JOIN orders ON clients_orders.order_id = orders.id
WHERE clients.age BETWEEN 18 AND 65
GROUP BY clients.id, clients.first_name, clients.last_name, clients.age
HAVING COUNT(DISTINCT orders.category) = 1 AND COUNT(orders.id) = 2;
