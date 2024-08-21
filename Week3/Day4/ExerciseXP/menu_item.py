from psycopg2 import sql

class Menu_Item:
    def __init__(self, cursor):
        self.cursor = cursor

    def add(self, name, price):
        """
        Insert a new item into the Menu_Items table.
        """
        self.cursor.execute(
            sql.SQL("""INSERT INTO Menu_Items (item_name, item_price)
                       VALUES (%s, %s)"""),
            [name, price]
        )
        print(f"Inserted {name} with price {price} into Menu_Items.")

    def delete(self, item_id):
        """
        Delete an item from the Menu_Items table based on its ID.
        """
        self.cursor.execute(
            sql.SQL("""DELETE FROM Menu_Items WHERE item_id = %s"""),
            [item_id]
        )
        print(f"Deleted item with ID {item_id} from Menu_Items.")

    def show(self, item_id):
        """
        Show a single item based on its ID.
        """
        self.cursor.execute(
            sql.SQL("""SELECT * FROM Menu_Items WHERE item_id = %s"""),
            [item_id]
        )
        result = self.cursor.fetchone()
        if result:
            print(result)
        else:
            print(f"No item found with ID {item_id}")

    def save_to_file(self, file_path):
        """
        Export the Menu_Items table to a CSV file.
        """
        self.cursor.execute(
            sql.SQL("""COPY Menu_Items (item_id, item_name, item_price)
                       TO %s WITH CSV HEADER DELIMITER ','"""),
            [file_path]
        )
        print(f"Saved Menu_Items to {file_path}.")
