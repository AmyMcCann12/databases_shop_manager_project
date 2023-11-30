DROP TABLE IF EXISTS items
DROP SEQUENCE IF EXISTS items_id_seq
DROP TABLE IF EXISTS orders
DROP SEQUENCE IF EXISTS orders_id_seq
DROP TABLE IF EXISTS items_orders

-- Create First table.
CREATE SEQUENCE IF NOT EXISTS items_id_seq
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  unit_price float,
  quantity int
);

-- Create the second table.
CREATE SEQUENCE IF NOT EXISTS orders_id_seq
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  order_date date
);

-- Create the join table.
CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

-- Add any records that are needed for the tests to run

INSERT INTO items (name, unit_price, quantity) VALUES ('Pepper', 0.79, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Cucumber', 0.5, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Fish', 3.49, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Chocolate Bar', 1.30, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Cereal', 2.2, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Ice Cream', 1.99, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Apples', 1.69, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Chips', 2.50, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Milk', 1.20, 5)
INSERT INTO items (name, unit_price, quantity) VALUES ('Cheese', 3.49, 5)

INSERT INTO orders (customer_name, order_date) VALUES ('Peppa Pig', 2023-10-21)
INSERT INTO orders (customer_name, order_date) VALUES ('Susie Sheep', 2023-09-21)
INSERT INTO orders (customer_name, order_date) VALUES ('Danny Dog', 2023-05-03)
INSERT INTO orders (customer_name, order_date) VALUES ('Wendy Wolf', 2023-09-13)
INSERT INTO orders (customer_name, order_date) VALUES ('Candy Cat', 2023-11-22)
INSERT INTO orders (customer_name, order_date) VALUES ('Rebecca Rabbit', 2023-04-09)

INSERT INTO items_orders (item_id, order_id) VALUES (1,2)
INSERT INTO items_orders (item_id, order_id) VALUES (2,1)
INSERT INTO items_orders (item_id, order_id) VALUES (3,4)
INSERT INTO items_orders (item_id, order_id) VALUES (5,2)
INSERT INTO items_orders (item_id, order_id) VALUES (6,5)
INSERT INTO items_orders (item_id, order_id) VALUES (4,6)
INSERT INTO items_orders (item_id, order_id) VALUES (7,4)
INSERT INTO items_orders (item_id, order_id) VALUES (8,3)
INSERT INTO items_orders (item_id, order_id) VALUES (9,2)
INSERT INTO items_orders (item_id, order_id) VALUES (10,1)
INSERT INTO items_orders (item_id, order_id) VALUES (1,3)
INSERT INTO items_orders (item_id, order_id) VALUES (2,4)
INSERT INTO items_orders (item_id, order_id) VALUES (3,2)
INSERT INTO items_orders (item_id, order_id) VALUES (4,6)
INSERT INTO items_orders (item_id, order_id) VALUES (5,5)