from lib.item import Item
from lib.item_repository import ItemRepository

"""
When we call ItemRepository#all
We get a list of Item objects
"""
def test_get_all_items(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    result = repository.all()
    assert result == [
        Item(1,'Pepper', 0.79, 5),
        Item(2,'Cucumber', 0.5, 5),
        Item(3,'Fish', 3.49, 5),
        Item(4,'Chocolate Bar', 1.30, 5),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 5),
        Item(7,'Apples', 1.69, 5),
        Item(8,'Chips', 2.50, 5),
        Item(9,'Milk', 1.20, 5),
        Item(10,'Cheese', 3.49, 5)
    ]

"""
When we call ItemRepository#find
We get a single Item object
"""

def test_find_single_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    result = repository.find('Fish')
    assert result == Item(3,'Fish', 3.49, 5)

"""
When we call ItemRepository#create
We get a new record in the database
"""

def test_create_new_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    repository.create(Item(11, 'Pizza', 4.50, 10))

    result = repository.all()
    assert result == [
        Item(1,'Pepper', 0.79, 5),
        Item(2,'Cucumber', 0.5, 5),
        Item(3,'Fish', 3.49, 5),
        Item(4,'Chocolate Bar', 1.30, 5),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 5),
        Item(7,'Apples', 1.69, 5),
        Item(8,'Chips', 2.50, 5),
        Item(9,'Milk', 1.20, 5),
        Item(10,'Cheese', 3.49, 5),
        Item(11, 'Pizza', 4.50, 10)
    ]

"""
When we call ItemRepository#delete
We can delete a record from the database
"""
def test_delete_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    repository.delete('Milk')
    result = repository.all()
    assert result == [
        Item(1,'Pepper', 0.79, 5),
        Item(2,'Cucumber', 0.5, 5),
        Item(3,'Fish', 3.49, 5),
        Item(4,'Chocolate Bar', 1.30, 5),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 5),
        Item(7,'Apples', 1.69, 5),
        Item(8,'Chips', 2.50, 5),
        Item(10,'Cheese', 3.49, 5),
    ]

"""
When we call #find_by_order with an order id
Then I get all the items which are linked to that order
"""

def test_find_by_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    result = repository.find_by_order(4)
    assert result == [
        Item(2,'Cucumber', 0.5, 5),
        Item(3,'Fish', 3.49, 5),
        Item(7,'Apples', 1.69, 5)
    ]