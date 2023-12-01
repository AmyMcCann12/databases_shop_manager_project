from lib.order import Order

class OrderRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM orders')
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer_name'], row['order_date'])
            orders.append(order)
        return orders
    
    def find(self, order_id):
        rows = self.connection.execute('SELECT * FROM orders WHERE id = %s', [order_id])
        return Order(rows[0]['id'], rows[0]['customer_name'], rows[0]['order_date'])
    
    def create(self, order):
        self.connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)', 
                                [order.customer_name, order.order_date])
        return None
    
    def find_by_item(self, item_id):
        rows = self.connection.execute(
            """SELECT orders.id, orders.customer_name, orders.order_date
            FROM orders
            JOIN items_orders ON items_orders.order_id = orders.id
            JOIN items ON items_orders.item_id = items.id
            WHERE items.id = %s""", [item_id])
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer_name'], row['order_date'])
            orders.append(order)
        return orders
    
    def delete(self, order_id):
        self.connection.execute('DELETE FROM orders WHERE id = %s', [order_id])
        return None