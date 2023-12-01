from lib.order import Order
from lib.order_repository import OrderRepository
import datetime

"""
When we call OrderRepository#all
We get a list of Order objects
"""
def test_get_all_orders(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    result = repository.all()
    assert result == [
        Order(1,'John Smith', datetime.date(2023,10,21)),       
        Order(2,'David Jones', datetime.date(2023,9,21)),
        Order(3,'Thomas Wolf', datetime.date(2023,5,3)),
        Order(4,'Hannah Smith', datetime.date(2023,9,13)),
        Order(5,'Frank Stow', datetime.date(2023,11,22)),
        Order(6,'Julie Wish', datetime.date(2023,4,9))
        ]

"""
When we call OrderRepository#find_by_customer
We get a single Order object
"""
def test_find(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    result = repository.find(3)
    assert result == Order(3,'Thomas Wolf', datetime.date(2023,5,3))

"""
When we call OrderRepository#create
We get a new record in the database
"""
def test_create_order_adds_to_order_table(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    repository.create(Order(7, 'Amy Moss', datetime.date(2023,11,30)))
    result = repository.all()
    assert result == [
        Order(1,'John Smith', datetime.date(2023,10,21)),       
        Order(2,'David Jones', datetime.date(2023,9,21)),
        Order(3,'Thomas Wolf', datetime.date(2023,5,3)),
        Order(4,'Hannah Smith', datetime.date(2023,9,13)),
        Order(5,'Frank Stow', datetime.date(2023,11,22)),
        Order(6,'Julie Wish', datetime.date(2023,4,9)),
        Order(7, 'Amy Moss', datetime.date(2023,11,30))
        ]

"""
When we call OrderRepository#delete
We can delete a record from the database
"""
def test_delete_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    repository.delete(2)
    result = repository.all()
    assert result == [
        Order(1,'John Smith', datetime.date(2023,10,21)),       
        Order(3,'Thomas Wolf', datetime.date(2023,5,3)),
        Order(4,'Hannah Smith', datetime.date(2023,9,13)),
        Order(5,'Frank Stow', datetime.date(2023,11,22)),
        Order(6,'Julie Wish', datetime.date(2023,4,9))
    ]

"""
When we call #find_by_item with an item name
Then I get all the Orders which are linked to that item
"""
def test_find_by_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repository = OrderRepository(db_connection)
    result = repository.find_by_item(3)
    assert result == [ 
        Order(2,'David Jones', datetime.date(2023,9,21)),
        Order(4,'Hannah Smith', datetime.date(2023,9,13))
    ]

