# main.py
from utils import Utils
from psycopg2 import sql
from menu_item import Menu_Item
from menu_editor import Menu_Editor

new_db_name = "w3d4_db"

try:
    Utils.db_high_level(new_db_name, 'create') # We need some additional non-obvious logic to create and drop databas
    conn = Utils.get_connection(new_db_name)
    conn.autocommit = True # Part of that non-obvious logic
    cursor = conn.cursor()

    # Create the Menu_Items table if it does not exist
    cursor.execute(sql.SQL("""
        CREATE TABLE IF NOT EXISTS Menu_Items (
            item_id SERIAL PRIMARY KEY, 
            item_name VARCHAR(30) NOT NULL, 
            item_price SMALLINT DEFAULT 0
        )
    """))

    menu_item_instance = Menu_Item(cursor)
    menu_item_instance.add("Cheeseburger", 10)
    menu_item_instance.add("Veggie Burger", 9)
    menu_item_instance.add("French Fries", 3)
    menu_item_instance.add("Coke", 2)
    menu_item_instance.add("Milkshake", 5)
    menu_item_instance.add("Chicken Salad", 7)
    menu_item_instance.add("Fish Tacos", 12)
    menu_item_instance.add("Chocolate Cake", 6)
    menu_item_instance.add("Coffee", 3)
    menu_item_instance.add("Iced Tea", 2)

    # Call the menu editor to show the user menu
    Menu_Editor.show_user_menu(cursor)

    cursor.close()
    conn.close()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    Utils.terminate_connections(new_db_name)
    Utils.db_high_level(new_db_name, 'delete')
