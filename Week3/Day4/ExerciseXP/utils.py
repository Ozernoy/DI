import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Utils:

    @staticmethod
    def db_high_level(new_db_name, intention):
        """
        We use this function to connect to the default DB to create or drop a DB.
        """
        conn = Utils.get_connection('postgres')
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        try:
            if intention == 'create':
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))
                print(f"Database {new_db_name} created successfully.")
            elif intention == 'delete':
                cursor.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(new_db_name)))
                print(f"Database {new_db_name} deleted successfully.")
        except Exception as e:
            print(f"An error occurred while trying to {intention} the database: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_connection(dbname):
        return psycopg2.connect(
            dbname=dbname,
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

    @staticmethod
    def terminate_connections(dbname):
        """
        Terminate all connections to the specified database.
        """
        conn = Utils.get_connection('postgres')
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        try:
            # Terminate all active connections to the database
            cursor.execute(sql.SQL(
                "SELECT pg_terminate_backend(pg_stat_activity.pid) "
                "FROM pg_stat_activity "
                "WHERE pg_stat_activity.datname = %s AND pid <> pg_backend_pid();"
            ), [dbname])
            print(f"Terminated all connections to the database {dbname}.")
        except Exception as e:
            print(f"An error occurred while trying to terminate connections: {e}")
        finally:
            cursor.close()
            conn.close()
