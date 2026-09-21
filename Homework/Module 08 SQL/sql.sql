CREATE TABLE estimate_items (
id INTEGER PRIMARY KEY, 
estimate_id INTEGER NOT NULL,
sku TEXT NOT NULL,
quantity INTEGER NOT NULL,
price_per_unit REAL NOT NULL,
FOREIGN KEY (estimate_id) REFERENCES estimates(id),
FOREIGN KEY (sku) REFERENCES equipment(sku)
);

CREATE TABLE estimates (
id INTEGER PRIMARY KEY,
project_name TEXT NOT NULL,
days INTEGER NOT NULL
);

INSERT INTO estimates (project_name, days)
VALUES ('Капитанская дочка', 21);

INSERT INTO estimate_items (estimate_id, sku, quantity, price_per_unit)
VALUES (1, 'LIGHT-0001', 3, 3500);

INSERT INTO estimate_items (estimate_id, sku, quantity, price_per_unit)
VALUES (1, 'STAND-0005', 6, 800);




SELECT * FROM equipment;

SELECT name, price_per_unit 
FROM equipment
WHERE category = 'HMI_LIGHT';

SELECT sku, name, available
FROM equipment
WHERE available >= 20;

SELECT sku, name, price_per_unit, available
FROM equipment
WHERE price_per_unit >= 1000 
    and available > 5;

SELECT name, category, available
FROM equipment
WHERE available > 0
ORDER BY available DESC
LIMIT 10;


SELECT MAX(price_per_unit)
FROM equipment;

SELECT SUM(available)
FROM equipment
WHERE category = 'STANDS';

SELECT COUNT(*)
FROM equipment
WHERE price_per_unit < 1000;



UPDATE equipment
SET price_per_unit = price_per_unit + 500
WHERE category = 'HMI_LIGHT';

UPDATE equipment
SET available = 0 
WHERE sku = 'LIGHT-0003';

DELETE FROM equipment
WHERE sku = 'CABLE-0001';




SELECT equipment.name, estimate_items.quantity, estimate_items.price_per_unit
FROM equipment
JOIN estimate_items
    ON equipment.sku = estimate_items.sku
WHERE estimate_id = 1
;




SELECT estimate_id, SUM(quantity * price_per_unit)
FROM estimate_items
GROUP BY estimate_id;

SELECT equipment.category, SUM(estimate_items.price_per_unit * estimate_items.quantity)
FROM estimate_items
JOIN equipment ON equipment.sku = estimate_items.sku
GROUP BY category;




SELECT estimates.project_name, SUM(estimate_items.quantity * estimate_items.price_per_unit) AS total_revenue
FROM estimate_items
JOIN estimates ON estimates.id = estimate_items.estimate_id
GROUP BY estimates.name
HAVING SUM(estimate_items.quantity * estimate_items.price_per_unit) > 10000;