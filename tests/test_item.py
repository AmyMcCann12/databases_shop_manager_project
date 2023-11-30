from lib.item import Item

"""
Item constructs with an id, name, unit price and quantity
"""

def test_item_constructs():
    item = Item(1, "Fish", 4.99, 3)
    assert item.id == 1
    item.name == "Fish"
    item.unit_price == 4.99
    item.quantity == 3

"""
We can format items to strings nicely
"""

def test_items_format_nicely():
    item = Item(1, "Fish", 4.99, 3)
    assert str(item) == "Item(1, Fish, 4.99, 3)"

"""
We can compare two identical items
and have them be equal
"""

def test_items_are_equal():
    item1 = Item(1, "Fish", 4.99, 3)
    item2 = Item(1, "Fish", 4.99, 3)
    assert item1 == item2