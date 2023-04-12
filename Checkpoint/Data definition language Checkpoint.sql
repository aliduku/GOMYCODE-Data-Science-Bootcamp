CREATE TABLE customers (
	customer_id INT PRIMARY KEY NOT NULL,
	name VARCHAR(200) NOT NULL,
	email VARCHAR(400) NOT NULL,
	address VARCHAR (500) NOT NULL
);

CREATE TABLE products (
	product_id INT PRIMARY KEY NOT NULL,
	name VARCHAR(200) NOT NULL,
	price DECIMAL(10, 2) NOT NULL CHECK (price > 0)
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY NOT NULL,
	customer_id INT NOT NULL,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	order_date DATE NOT NULL,
	CONSTRAINT cust_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	CONSTRAINT prod_id FOREIGN KEY (product_id) REFERENCES products(product_id)
);