from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM items')
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], row['unit_price'], row['quantity'])
            items.append(item)
        return items
    
    def find(self, item_id):
        rows = self.connection.execute(
            'SELECT * FROM items WHERE id = %s', [item_id])
        return Item(rows[0]['id'], rows[0]['name'], rows[0]['unit_price'], rows[0]['quantity'])
    
    def create(self, item):
        self.connection.execute(
            'INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity]
        )
        return None
    
    def delete(self, item_name):
        self.connection.execute(
            'DELETE FROM items WHERE name = %s', [item_name]
        )
        return None
    
    def find_by_order(self, order_id):
        rows = self.connection.execute(
            """SELECT items.id, items.name, items.unit_price, items.quantity
            FROM items
            JOIN items_orders ON items_orders.item_id = items.id
            JOIN orders ON items_orders.order_id = orders.id
            WHERE orders.id = %s""", [order_id]
        )
        items_by_order = []
        for row in rows:
            item = Item(row['id'], row['name'], row['unit_price'], row['quantity'])
            items_by_order.append(item)
        return items_by_order
    
    def add_item_to_order(self, item_id, order_id):
        self.connection.execute(
            'INSERT INTO items_orders (item_id, order_id) VALUES (%s, %s)', [item_id, order_id]
        )
        return None
    
    def remove_item_from_order(self, id_item, id_order):
        self.connection.execute(
            'DELETE FROM items_orders WHERE item_id = %s AND order_id = %s', [id_item, id_order]
        )
        return None