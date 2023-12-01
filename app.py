from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from lib.item import Item
from lib.order import Order

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/items_orders.sql")

    def run(self):
        item_repository = ItemRepository(self._connection)
        order_repository = OrderRepository(self._connection)
        options = """
        1 = List all shop items
        2 = Look at which orders contain a particular item
        3 = List all orders
        4 = Look at the list of items in a particular order
        5 = Create a new item
        6 = Create a new order
        7 = Add a new item to an order
        8 = Exit program\n"""
        input_text = "Enter the number of your choice: "
        def follow_up():
            question_after_task = input('\nIs there anything else you would like to do in the shop manager program (Y/N)? ')
            while question_after_task not in ['Y', 'y', 'N', 'n']:
                question_after_task = input("Incorrect input, must be Y or N, please try again: ")
            if question_after_task in ['Y', 'y']:
                print("What would you like to do next?")
                print(options)
                return input(input_text)
            else:
                return '8'
        def full_item_to_print(item):
            return f"#{item.id} {item.name} - Unit Price: {item.unit_price} - Quantity: {item.quantity}"
        def full_order_to_print(order):
            return f"#{order.id} {order.customer_name} - Order Date: {order.order_date}"
        print('Welcome to the shop management program!\n')
        print('What would you like to do?')
        print(options)
        response = input(input_text)
        while response in ['1', '2', '3', '4', '5', '6', '7']:
            if response == '1':
                items = item_repository.all()
                print("\nHere is a list of all the shop items:\n")
                for item in items:
                    print(full_item_to_print(item))
                response = follow_up()
            elif response == '2':
                item_id = input("Enter the id number of the item you would like to search by: ")
                orders = order_repository.find_by_item(item_id)
                print("\nHere is a list of the orders containing item number %s:" %item_id)
                for order in orders:
                    print(full_order_to_print(order))
                response = follow_up()
            elif response == '3':
                orders = order_repository.all()
                print("\nHere is a list of all the orders:\n")
                for order in orders:
                    print(full_order_to_print(order))
                response = follow_up()
            elif response == '4':
                order_id = input("Enter the id number of the order you would like to look at: ")
                items = item_repository.find_by_order(order_id)
                print("\nHere is a list of items contained in order number %s:" %order_id)
                for item in items:
                    print(f"#{item.id} {item.name} - Unit Price: {item.unit_price}")
                response = follow_up()
            elif response == '5':
                item_name = input("Enter the name of the item you would like to create: ")
                item_unit_price = input("Enter the unit price of the item you would like to create: ")
                item_quantity = input("What is the quantity of this item: ")
                item_repository.create(Item(None, item_name, item_unit_price, item_quantity))
                print("\nThe following item has now been created:")
                item_id = len(item_repository.all())
                item = item_repository.find(item_id)
                print(full_item_to_print(item))
                response = follow_up()
            elif response == '6':
                customer_name = input("Enter the name of the customer for the order: ")
                order_date = input("Enter the date of the order (YYYY-MM-DD): ")
                order_repository.create(Order(None, customer_name, order_date))
                print("\nThe following order has now been created:")
                order_id = len(order_repository.all())
                order = order_repository.find(order_id)
                print(full_order_to_print(order))
                response = follow_up()
            elif response == '7':
                order_id = input("Enter the id number of the order you would like to update: ")
                item_id = input("Enter the id number of the item you would like to add: ")
                item_repository.add_item_to_order(item_id, order_id)
                print('\nThe following item has been added to order number %s:' %order_id)
                item = item_repository.find(item_id)
                print(full_item_to_print(item))
                response = follow_up()
        else: 
            print('\nThank you for using the shop management program today, your session has now ended.\n')

if __name__ == '__main__':
    app = Application()
    app.run()