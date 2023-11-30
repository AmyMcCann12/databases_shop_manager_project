from lib.order import Order
import datetime

"""
Order constructs with an id, customer name and order date
"""

def test_order_constructs():
    order = Order(1, "John Smith", datetime.date(2023,10,12))
    assert order.id == 1
    assert order.customer_name == "John Smith"
    assert order.order_date == datetime.date(2023,10,12)

"""
We can format orders to strings nicely
"""

def test_order_formats_nicely():
    order = Order(1, "John Smith", datetime.date(2023,10,12))
    assert str(order) == "Order(1, John Smith, 2023-10-12)"

"""
We can compare two identical orders
and have them be equal
"""

def test_orders_are_equal():
    order1 = Order(1, "John Smith", datetime.date(2023,10,12))
    order2 = Order(1, "John Smith", datetime.date(2023,10,12))
    assert order1 == order2