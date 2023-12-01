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
        Item(2,'Cucumber', 0.5, 30),
        Item(3,'Fish', 3.49, 3),
        Item(4,'Chocolate Bar', 1.30, 2),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 10),
        Item(7,'Apples', 1.69, 15),
        Item(8,'Chips', 2.50, 7),
        Item(9,'Milk', 1.20, 12),
        Item(10,'Cheese', 3.49, 9)
    ]

"""
When we call ItemRepository#find
We get a single Item object
"""
def test_find_single_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    result = repository.find(3)
    assert result == Item(3,'Fish', 3.49, 3)

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
        Item(2,'Cucumber', 0.5, 30),
        Item(3,'Fish', 3.49, 3),
        Item(4,'Chocolate Bar', 1.30, 2),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 10),
        Item(7,'Apples', 1.69, 15),
        Item(8,'Chips', 2.50, 7),
        Item(9,'Milk', 1.20, 12),
        Item(10,'Cheese', 3.49, 9),
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
        Item(2,'Cucumber', 0.5, 30),
        Item(3,'Fish', 3.49, 3),
        Item(4,'Chocolate Bar', 1.30, 2),
        Item(5,'Cereal', 2.2, 5),
        Item(6,'Ice Cream', 1.99, 10),
        Item(7,'Apples', 1.69, 15),
        Item(8,'Chips', 2.50, 7),
        Item(10,'Cheese', 3.49, 9),
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
        Item(2,'Cucumber', 0.5, 30),
        Item(3,'Fish', 3.49, 3),
        Item(7,'Apples', 1.69, 15)
    ]

"""
When we call ItemRepository#add_item_to_order
our join table is updated to link the items included in the order
"""
def test_add_item_to_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    repository.add_item_to_order(3, 6)
    result = repository.find_by_order(6)
    assert result == [
        Item(3, 'Fish', 3.49, 3),
        Item(4,'Chocolate Bar', 1.30, 2)
    ]

"""
When we call ItemRepository#remove_from_order
our join table is updated to link the items remove the item from the order
"""
def test_remove_item_from_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = ItemRepository(db_connection)
    repository.remove_item_from_order(3, 4)
    result = repository.find_by_order(4)
    assert result == [
        Item(2,'Cucumber', 0.5, 30),
        Item(7,'Apples', 1.69, 15)
    ]