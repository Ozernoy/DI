from menu_item import Menu_Item
from psycopg2 import sql

class Menu_Editor:

    @staticmethod
    def show_user_menu(cursor):
        while True:
            inp_str = input(
                '''
                View an Item (V)
                Add an Item (A)
                Delete an Item (D)
                Update an Item (U)
                Show the Menu (S)
                Exit (E)
                '''
            ).upper()

            if inp_str == 'V':
                Menu_Editor.show_item(cursor)
            elif inp_str == 'A':
                Menu_Editor.add_item(cursor)
            elif inp_str == 'D':
                Menu_Editor.delete_item(cursor)
            elif inp_str == 'U':
                Menu_Editor.update_item(cursor)
            elif inp_str == 'S':
                Menu_Editor.show_all_items(cursor)
            elif inp_str == 'E':
                break
            else:
                print("Invalid option. Please try again.")

    @staticmethod
    def show_item(cursor):
        mi = Menu_Item(cursor)
        item_id = int(input('Input the ID: '))
        mi.show(item_id)

    @staticmethod
    def add_item(cursor):
        name = input('Input the name of the new product: ')
        price = int(input('Input the price of the new product: '))
        mi = Menu_Item(cursor)
        mi.add(name, price)

    @staticmethod
    def delete_item(cursor):
        item_id = int(input('Input the ID of the product to delete: '))
        mi = Menu_Item(cursor)
        mi.delete(item_id)

    @staticmethod
    def update_item(cursor):
        item_id = int(input('Input the ID of the product to update: '))
        new_name = input('Input the new name of the product: ')
        new_price = int(input('Input the new price of the product: '))
        cursor.execute(
            sql.SQL("""UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_id = %s"""),
            [new_name, new_price, item_id]
        )
        print(f"Updated item with ID {item_id} to name {new_name} and price {new_price}.")

    @staticmethod
    def show_all_items(cursor):
        cursor.execute(
            sql.SQL("""SELECT * FROM Menu_Items""")
        )
        items = cursor.fetchall()
        for item in items:
            print(item)
