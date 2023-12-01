DROP TABLE IF EXISTS items_orders;
DROP TABLE IF EXISTS items;
DROP SEQUENCE IF EXISTS items_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;


-- Create First table.
CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  unit_price float,
  quantity int
);

-- Create the second table.
CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
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

INSERT INTO items (name, unit_price, quantity) VALUES ('Pepper', 0.79, 5);
INSERT INTO items (name, unit_price, quantity) VALUES ('Cucumber', 0.5, 30);
INSERT INTO items (name, unit_price, quantity) VALUES ('Fish', 3.49, 3);
INSERT INTO items (name, unit_price, quantity) VALUES ('Chocolate Bar', 1.30, 2);
INSERT INTO items (name, unit_price, quantity) VALUES ('Cereal', 2.2, 5);
INSERT INTO items (name, unit_price, quantity) VALUES ('Ice Cream', 1.99, 10);
INSERT INTO items (name, unit_price, quantity) VALUES ('Apples', 1.69, 15);
INSERT INTO items (name, unit_price, quantity) VALUES ('Chips', 2.50, 7);
INSERT INTO items (name, unit_price, quantity) VALUES ('Milk', 1.20, 12);
INSERT INTO items (name, unit_price, quantity) VALUES ('Cheese', 3.49, 9);

INSERT INTO orders (customer_name, order_date) VALUES ('John Smith', '2023-10-21');
INSERT INTO orders (customer_name, order_date) VALUES ('David Jones', '2023-09-21');
INSERT INTO orders (customer_name, order_date) VALUES ('Thomas Wolf', '2023-05-03');
INSERT INTO orders (customer_name, order_date) VALUES ('Hannah Smith', '2023-09-13');
INSERT INTO orders (customer_name, order_date) VALUES ('Frank Stow', '2023-11-22');
INSERT INTO orders (customer_name, order_date) VALUES ('Julie Wish', '2023-04-09');

INSERT INTO items_orders (item_id, order_id) VALUES (1,2);
INSERT INTO items_orders (item_id, order_id) VALUES (2,1);
INSERT INTO items_orders (item_id, order_id) VALUES (3,4);
INSERT INTO items_orders (item_id, order_id) VALUES (5,2);
INSERT INTO items_orders (item_id, order_id) VALUES (6,5);
INSERT INTO items_orders (item_id, order_id) VALUES (4,6);
INSERT INTO items_orders (item_id, order_id) VALUES (7,4);
INSERT INTO items_orders (item_id, order_id) VALUES (8,3);
INSERT INTO items_orders (item_id, order_id) VALUES (9,2);
INSERT INTO items_orders (item_id, order_id) VALUES (10,1);
INSERT INTO items_orders (item_id, order_id) VALUES (1,3);
INSERT INTO items_orders (item_id, order_id) VALUES (2,4);
INSERT INTO items_orders (item_id, order_id) VALUES (3,2);
INSERT INTO items_orders (item_id, order_id) VALUES (4,3);
INSERT INTO items_orders (item_id, order_id) VALUES (5,5);