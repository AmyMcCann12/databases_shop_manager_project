


"""
When we call OrderRepository#all
We get a list of Order objects
"""


"""
When we call OrderRepository#find
We get a single Order object
"""

"""
When we call OrderRepository#create
We get a new record in the database
"""

"""
When we call OrderRepository#create
our join table is also updated to link the items included in the order
"""

"""
When we call OrderRepository#delete
We can delete a record from the database
"""

"""
When we call #find_by_item with an item name
Then I get all the Orders which are linked to that item
"""