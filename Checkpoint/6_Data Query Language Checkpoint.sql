-- Create Customer table
CREATE TABLE Customer (Customer_id INT PRIMARY KEY, customer_Name VARCHAR(50), customer_Tel VARCHAR(15));

-- Create Product table
CREATE TABLE Product (Product_id INT PRIMARY KEY, product_name VARCHAR(50), category VARCHAR(50), Price DECIMAL(10, 2));

-- Create Orders table
CREATE TABLE Orders (Customer_id INT, Product_id INT, OrderDate DATE, quantity INT, total_amount DECIMAL(10, 2),
    FOREIGN KEY (Customer_id) REFERENCES Customer (Customer_id),
    FOREIGN KEY (Product_id) REFERENCES Product (Product_id)
);

-- Insert data into Customer table
INSERT INTO Customer (Customer_id, customer_Name, customer_Tel)
VALUES (1, 'John Doe', '1234567890'),
       (2, 'Jane Smith', '9876543210'),
       (3, 'Alice Johnson', '4567890123'),
       (4, 'Bob Williams', '7890123456'),
       (5, 'Charlie Brown', '2345678901'),
       (6, 'Eve Adams', '8765432109');

-- Insert data into Product table
INSERT INTO Product (Product_id, product_name, category, Price)
VALUES (1, 'Gadget', 'Electronics', 49.99),
       (2, 'Widget', 'Tools', 19.99),
       (3, 'Doohickey', 'Hardware', 9.99),
       (4, 'Random Product', 'Miscellaneous', 14.99),
       (5, 'Tech Gizmo', 'Electronics', 39.99),
       (6, 'Handy Tool', 'Tools', 15.99),
       (7, 'Hardware Item', 'Hardware', 7.99),
       (8, 'Miscellaneous Product', 'Miscellaneous', 24.99);

-- Insert data into Orders table
INSERT INTO Orders (Customer_id, Product_id, OrderDate, quantity, total_amount)
VALUES (1, 1, '2023-04-14', 2, 99.98),
       (2, 2, '2023-04-14', 1, 19.99),
       (3, 3, '2023-04-14', 3, 29.97),
       (4, 4, '2023-04-14', 5, 74.95),
       (1, 2, '2023-04-14', 3, 59.97),
       (2, 3, '2023-04-14', 1, 9.99),
       (3, 4, '2023-04-14', 2, 29.98),
       (4, 5, '2023-04-14', 1, 39.99),
       (5, 6, '2023-04-14', 4, 63.96),
       (6, 7, '2023-04-14', 3, 23.97);

-- Query 1
SELECT Customer.customer_Name, 
       SUM(CASE WHEN Product.product_name = 'Widget' THEN Orders.quantity * Product.Price ELSE 0 END) AS widget_cost,
       SUM(CASE WHEN Product.product_name = 'Gadget' THEN Orders.quantity * Product.Price ELSE 0 END) AS gadget_cost,
       SUM(CASE WHEN Product.product_name IN ('Widget', 'Gadget') THEN Orders.quantity * Product.Price ELSE 0 END) AS total_cost
FROM Customer, Orders, Product
WHERE Customer.Customer_id = Orders.Customer_id
  AND Orders.Product_id = Product.Product_id
  AND Product.product_name IN ('Widget', 'Gadget')
GROUP BY Customer.customer_Name
HAVING SUM(CASE WHEN Product.product_name = 'Widget' THEN Orders.quantity ELSE 0 END) >= 1
   AND SUM(CASE WHEN Product.product_name = 'Gadget' THEN Orders.quantity ELSE 0 END) >= 1;

-- Query 2
SELECT Customer.customer_Name, SUM(Product.Price * Orders.quantity) AS total_widget_cost
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
JOIN Product ON Orders.Product_id = Product.Product_id
WHERE Product.product_name = 'Widget'
GROUP BY Customer.customer_Name
HAVING SUM(Orders.quantity) >= 1;

-- Query 3
SELECT Customer.customer_Name, SUM(Product.Price * Orders.quantity) AS total_gadget_cost
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
JOIN Product ON Orders.Product_id = Product.Product_id
WHERE Product.product_name = 'Gadget'
GROUP BY Customer.customer_Name
HAVING SUM(Orders.quantity) >= 1;

-- Query 4
SELECT Customer.customer_Name, SUM(Product.Price * Orders.quantity) AS total_doohickey_cost
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
JOIN Product ON Orders.Product_id = Product.Product_id
WHERE Product.product_name = 'Doohickey'
GROUP BY Customer.customer_Name
HAVING SUM(Orders.quantity) >= 1;

-- Query 5
SELECT Customer.customer_Name,
       SUM(CASE WHEN Product.product_name = 'Widget' THEN Orders.quantity ELSE 0 END) AS total_widgets_ordered,
       SUM(CASE WHEN Product.product_name = 'Gadget' THEN Orders.quantity ELSE 0 END) AS total_gadgets_ordered,
	   SUM(Orders.quantity) AS total_products_ordered,
       SUM(Product.Price * Orders.quantity) AS total_order_cost
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
JOIN Product ON Orders.Product_id = Product.Product_id
WHERE Product.product_name IN ('Widget', 'Gadget')
GROUP BY Customer.customer_Name;

-- Query 6
SELECT Product.product_name, SUM(Orders.quantity) AS total_quantity_ordered
FROM Product
JOIN Orders ON Product.Product_id = Orders.Product_id
GROUP BY Product.product_name
HAVING SUM(Orders.quantity) >= 1;

-- Query 7
SELECT Customer.customer_Name, COUNT(*) AS total_orders_placed
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
GROUP BY Customer.customer_Name
HAVING COUNT(*) = (
  SELECT TOP 1 COUNT(*)
  FROM Orders
  GROUP BY Customer_id
  ORDER BY COUNT(*) DESC
);

-- Query 8
SELECT Product.product_name, SUM(Orders.quantity) AS total_products_ordered
FROM Product
JOIN Orders ON Product.Product_id = Orders.Product_id
GROUP BY Product.product_name
HAVING SUM(Orders.quantity) = (
  SELECT TOP 1 SUM(quantity)
  FROM Orders
  GROUP BY Product_id
  ORDER BY SUM(quantity) DESC
);

-- Query 9
SELECT Customer.customer_Name, COUNT(*) AS total_orders_placed
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
GROUP BY Customer.customer_Name
HAVING COUNT(DISTINCT DATEPART(WEEKDAY, Orders.OrderDate)) = 7;
